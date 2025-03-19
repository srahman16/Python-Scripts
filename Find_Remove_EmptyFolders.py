'''Title: Script to Identify Empty Folders in a Directory
Author: Shahriar Rahman
Version: 2
Date: 20 March 2025'''

import os

def get_empty_folders(directory):
    empty_folders = []
    for root, dirs, files in os.walk(directory):
        for d in dirs:
            folder_path = os.path.join(root, d)
            if not os.listdir(folder_path):
                empty_folders.append(folder_path)
    return empty_folders

directory = r"X:\Prefire"
output_file = os.path.join(directory, "empty_folders.txt")

empty_folders = get_empty_folders(directory)

with open(output_file, "w") as f:
    for folder in empty_folders:
        f.write(folder + "\n")

for folder in empty_folders:
    os.rmdir(folder)

print(f"Empty folders have been listed in {output_file} and deleted.")
