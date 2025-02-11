import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import os
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from keras._tf_keras.keras.models import load_model

# Load the pre-trained model
model = load_model("model_checkpoint.h5")

IMG_SIZE = 128
scaler = MinMaxScaler()
encoder = OneHotEncoder(sparse_output=False, handle_unknown="ignore")

# Define class names for the different diagnoses
class_names = [
    "Actinic keratosis",
    "Basal cell carcinoma",
    "Benign keratosis",
    "Dermatofibroma",
    "Melanoma",
    "Nevus",
    "Seborrheic keratosis"
]

# Preprocessing
def preprocess_image(image):
    # Convert the image to RGB
    img = image.convert("RGB")
    
    # Augmentation
    img = img.resize((IMG_SIZE, IMG_SIZE))
    img = np.array(img) / 255.0  # Normalize
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

# Preprocess age and gender data
def preprocess_tabular_data(age, gender):
    # Normalize the age
    age = scaler.fit_transform(np.array([[age]]))  # Normalize age
    gender_one_hot = encoder.fit_transform(np.array([[gender]]))  # One-hot encoding for gender
    # Simulate missing features 
    additional_features = np.zeros((1, 17)) 
    return np.hstack([age, gender_one_hot, additional_features])

# Prediction function
def predict_skin_condition(image, age, gender):
    # Preprocess the image and tabular data
    image_data = preprocess_image(image)
    tabular_data = preprocess_tabular_data(age, gender)
    
    prediction = model.predict([image_data, tabular_data])
    
    predicted_class = np.argmax(prediction, axis=1)
    return predicted_class[0]  # Return the predicted class

# Save image and information into uploaded_images
def save_image_and_info(uploaded_file, age, gender):
    upload_path = "uploaded_images"
    if not os.path.exists(upload_path):
        os.makedirs(upload_path)
    
    image_path = os.path.join(upload_path, "image.jpg")
    txt_file_path = os.path.join(upload_path, "age_gender.txt")
    
    if os.path.exists(image_path):
        os.remove(image_path)
    if os.path.exists(txt_file_path):
        os.remove(txt_file_path)
    
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    with open(txt_file_path, "w") as f:
        f.write(f"{age}\n{gender}")

    return image_path, txt_file_path

def main():
    st.title("DermaScan: Dermatological Condition Detection")
    
    st.write("Upload your image and let the AI analyze it to detect potential skin conditions!")
    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    st.subheader("Enter your Age:")
    age = st.number_input("Age", min_value=1, max_value=100, value=25, step=1)

    st.subheader("Select your Gender:")
    gender = st.radio("Gender", options=["Male", "Female"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)
        
        saved_image_path, saved_txt_path = save_image_and_info(uploaded_file, age, gender)
        
        prediction = predict_skin_condition(image, age, gender)
        
        predicted_condition = class_names[prediction]
        st.write(f"Prediction: Possible dermatological condition: {predicted_condition}")

if __name__ == "__main__":
    main()
