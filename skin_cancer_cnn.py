
import numpy as np
import pandas as pd
import tensorflow as tf
import os
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.model_selection import train_test_split
from keras._tf_keras.keras.models import Model
from keras._tf_keras.keras.layers import (
    Input,
    Conv2D,
    MaxPooling2D,
    Flatten,
    Dense,
    Dropout,
    BatchNormalization,
    Concatenate,
)
from keras._tf_keras.keras.optimizers import Adam
from keras._tf_keras.keras.callbacks import ModelCheckpoint, ReduceLROnPlateau
from keras._tf_keras.keras.preprocessing.image import ImageDataGenerator

# Clear terminal
os.system("cls" if os.name == "nt" else "clear")
epoch_val = int(input("Enter epoch value: "))

# Load dataset
DATA_DIR = "../ham10000/HAM10000_images"
metadata = pd.read_csv("../ham10000/HAM10000_metadata.csv")
metadata["image_id"] += ".jpg"

# Image preprocessing
IMG_SIZE = 128
BATCH_SIZE = 32
data_gen = ImageDataGenerator(
    rescale=1.0 / 255,
    validation_split=0.2,
    horizontal_flip=True,
    rotation_range=15,
    zoom_range=0.2,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
)

# Tabular data preprocessing
metadata = metadata.dropna(subset=["age"])
scaler = MinMaxScaler()
metadata["age"] = scaler.fit_transform(metadata["age"].values.reshape(-1, 1))
encoder = OneHotEncoder(sparse_output=False, handle_unknown="ignore")
categorical_features = encoder.fit_transform(metadata[["sex", "localization"]])
tabular_features = np.hstack(
    [metadata["age"].values.reshape(-1, 1), categorical_features]
)

# Train-validation split
train_metadata, val_metadata = train_test_split(
    metadata, test_size=0.2, stratify=metadata["dx"], random_state=42
)
train_data = data_gen.flow_from_dataframe(
    train_metadata,
    DATA_DIR,
    x_col="image_id",
    y_col="dx",
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    subset="training",
    shuffle=True,
)
val_data = data_gen.flow_from_dataframe(
    val_metadata,
    DATA_DIR,
    x_col="image_id",
    y_col="dx",
    target_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    shuffle=True,
)

# Align the class indices
train_data.class_indices = {
    cls: idx for idx, cls in enumerate(sorted(metadata["dx"].unique()))
}
val_data.class_indices = train_data.class_indices

labels = pd.get_dummies(metadata["dx"])
labels = labels.reindex(columns=train_data.class_indices.keys(), fill_value=0).values
Y_train, Y_val = train_test_split(
    labels, test_size=0.2, stratify=metadata["dx"], random_state=42
)


# Extract the images and labels
def extract_images_and_labels(generator):
    images, labels = [], []
    for i in range(len(generator)):
        batch_images, batch_labels = generator[i]
        images.append(batch_images)
        labels.append(batch_labels)
    return np.vstack(images), np.vstack(labels)


X_train_images, Y_train = extract_images_and_labels(train_data)
X_val_images, Y_val = extract_images_and_labels(val_data)
X_train_tabular, X_val_tabular = (
    tabular_features[: len(X_train_images)],
    tabular_features[len(X_train_images) :],
)

# Ensure that the data is aligned
min_train_size = min(len(X_train_images), len(X_train_tabular), len(Y_train))
X_train_images, X_train_tabular, Y_train = (
    X_train_images[:min_train_size],
    X_train_tabular[:min_train_size],
    Y_train[:min_train_size],
)
min_val_size = min(len(X_val_images), len(X_val_tabular), len(Y_val))
X_val_images, X_val_tabular, Y_val = (
    X_val_images[:min_val_size],
    X_val_tabular[:min_val_size],
    Y_val[:min_val_size],
)

# Beginning of the CNN Model code
image_input = Input(shape=(IMG_SIZE, IMG_SIZE, 3), name="image_input")
x = Conv2D(32, (3, 3), activation="relu")(image_input)
x = MaxPooling2D(2, 2)(x)
x = BatchNormalization()(x)
x = Conv2D(64, (3, 3), activation="relu")(x)
x = MaxPooling2D(2, 2)(x)
x = BatchNormalization()(x)
x = Conv2D(128, (3, 3), activation="relu")(x)
x = MaxPooling2D(2, 2)(x)
x = BatchNormalization()(x)
x = Flatten()(x)
x = Dense(128, activation="relu")(x)

# Tabular model
tabular_input = Input(shape=(tabular_features.shape[1],), name="tabular_input")
y = Dense(16, activation="relu")(tabular_input)
y = Dense(32, activation="relu")(y)

merged = Concatenate()([x, y])
merged = Dense(128, activation="relu")(merged)
merged = Dropout(0.5)(merged)
output = Dense(len(train_data.class_indices), activation="softmax")(merged)
model = Model(inputs=[image_input, tabular_input], outputs=output)

# Compile the model
model.compile(
    optimizer=Adam(learning_rate=0.0001),
    loss="categorical_crossentropy",
    metrics=["accuracy"],
)

# Check if the model_checkpoint.h5 exists and remove it if it does
checkpoint_path = "model_checkpoint.h5"
if os.path.exists(checkpoint_path):
    os.remove(checkpoint_path)
    print(f"Removed existing {checkpoint_path} file.")

checkpoint = ModelCheckpoint(
    checkpoint_path, monitor="val_loss", save_best_only=True, verbose=1
)
lr_scheduler = ReduceLROnPlateau(monitor="val_loss", factor=0.5, patience=3)

# Train the model
history = model.fit(
    [X_train_images, X_train_tabular],
    Y_train,
    validation_data=([X_val_images, X_val_tabular], Y_val),
    epochs=epoch_val,
    batch_size=BATCH_SIZE,
    callbacks=[checkpoint, lr_scheduler],
)

# Evaluate the model, outputting a graph
test_images, test_labels = extract_images_and_labels(val_data)
test_tabular_data = X_val_tabular[: len(test_images)]
test_labels = test_labels[: len(test_images)]
predictions = model.predict([test_images, test_tabular_data])
predicted_classes = np.argmax(predictions, axis=1)
actual_classes = np.argmax(test_labels, axis=1)
test_accuracy = np.mean(predicted_classes == actual_classes)
print(f"Test Accuracy: {test_accuracy:.4f}")


