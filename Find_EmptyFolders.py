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
empty_folders = get_empty_folders(directory)

for folder in empty_folders:
    print(folder)
