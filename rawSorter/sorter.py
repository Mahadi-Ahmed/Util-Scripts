#!/usr/bin/python3

import os
import shutil

def organize_raw_files(input_dir, output_dir):
    # Check if the output directory exists, if not, create it
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterate through all files in the input directory
    for filename in os.listdir(input_dir):
        # Get the full path of the file
        file_path = os.path.join(input_dir, filename)

        # Check if it's a file and its extension is RAW
        if os.path.isfile(file_path) and filename.lower().endswith('.raf'):

            # Move the file to the new directory
            shutil.move(file_path, os.path.join(output_directory, filename))
            print(f"Moved {filename} to {output_directory}")

# Replace 'input_directory' and 'output_directory' with your actual directory paths
input_directory = '/Users/mahadiahmed/Pictures/fujifilm/101-FUJI'
output_directory = '/Users/mahadiahmed/Pictures/fujifilm/101-FUJI/rawFiles'

organize_raw_files(input_directory, output_directory)
