import os
import requests
from datetime import datetime
import json

# Load Instagram API configuration
with open('users.json', 'r') as f:
    users = json.load(f)
print(len(users))

import os

# Path to the directory containing user folders
images_directory = 'images'

# Dictionary to store the count of images per username
image_counts = {}

# Iterate over the folders in the images directory
for username_folder in os.listdir(images_directory):
    # Construct the full path to the username folder
    username_folder_path = os.path.join(images_directory, username_folder)
     
    # Check if the item in the directory is a folder
    if os.path.isdir(username_folder_path):
        # Count the number of files in the folder
        num_images = len(os.listdir(username_folder_path))
        
        # Store the count in the image_counts dictionary
        image_counts[username_folder] = num_images

# Print the image counts per username folder
for username, count in image_counts.items():
    print(f"{username}: {count} images")
