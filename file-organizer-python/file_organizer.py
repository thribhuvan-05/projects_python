import os
import shutil

# Folder path to organize
path = input("Enter folder path to organize: ")

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Audio": [".mp3", ".wav"],
    "Programs": [".py", ".java", ".cpp"]
}

# Read files in folder
files = os.listdir(path)

for file in files:
    filename, extension = os.path.splitext(file)

    for folder_name, extensions in file_types.items():
        if extension.lower() in extensions:

            folder_path = os.path.join(path, folder_name)

            # Create folder if it doesn't exist
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # Move file
            shutil.move(os.path.join(path, file), os.path.join(folder_path, file))

            print(f"Moved {file} → {folder_name}")