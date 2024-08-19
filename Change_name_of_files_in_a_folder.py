'''
Title: Change of filenames based on the parts of the existing filenames (no change in extension) and move into a different folder
Author: Shahriar Rahman
Email: shahriar.env12@gmail.com
'''

import os
import shutil

# input and output locations
input_folder = r'C:\your_input_folder'  
output_folder = r'C:\your_output_folder'  

# function to extract name
def extract_name(file_name):
    parts = file_name.split('_')
    if len(parts) >= 2:
        return f"{parts[1]}_{parts[2]}"
    return ""
# function to rename and move file
def rename_and_move_file(file_name, new_name, input_folder, output_folder):
    old_file_path = os.path.join(input_folder, file_name)
    file_extension = os.path.splitext(file_name)[1]  # according to your file extension
    new_file_path = os.path.join(output_folder, f"{new_name}{file_extension}")

    shutil.copy2(old_file_path, new_file_path) #copy the file into new location (folder)
    print(f"Copied: {new_file_path}")
# function to create a directory if not exists, and then process files in folder
def process_files_in_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for file_name in os.listdir(input_folder):
        if os.path.isfile(os.path.join(input_folder, file_name)):
            name = extract_name(file_name)
            if name:
                rename_and_move_file(file_name, name, input_folder, output_folder)

process_files_in_folder(input_folder, output_folder)
### End of script ###
