# We are utilizing Google Drive as a Cloud Storage Space to keep all the files in the dataset 'ham10000'
# We are using this method to keep data because GitHub wouldn't let us upload 5gb worth of content in a single repo :(
# Put the ham10000 folder inside a preceding directory from DermaScan folder (i.e. the folder before DermaScan)

import gdown  # Install via pip install gdown

# Google Drive file ID (Get from the shareable link)
file_id = "your_file_id_here"
destination = "data/dataset.zip"

# Download dataset (should download as a zip file)
gdown.download("https://drive.google.com/drive/folders/1vL3aKd1rUymI9HNBoJRaiaT5x8FRoCOt?usp=sharing", destination, quiet=False)
