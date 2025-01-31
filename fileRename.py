import os
import glob

# Define the root directory
root_directory = './Dataset'
# Function to remove whitespace from filenames in a directory
def remove_whitespace_from_filenames(directory):
    # List all files and directories in the current directory
    for filename in os.listdir(directory):
        # Get the full path of the file/directory
        full_path = os.path.join(directory, filename)
        
        # If it's a directory, recursively process it
        if os.path.isdir(full_path):
            remove_whitespace_from_filenames(full_path)
        # If it's a file, rename it to remove whitespace
        else:
            # Remove whitespace from the filename
            # new_filename = filename.replace(" ", "")
            new_filename = filename.replace("&", "")
            # new_filename = filename.replace("(", "")
            # new_filename = filename.replace(")", "")
            # new_filename = filename.replace(",", "")
            
            # Rename the file if the new filename is different
            if new_filename != filename:
                new_full_path = os.path.join(directory, new_filename)
                os.rename(full_path, new_full_path)
                print(f'Renamed: {full_path} -> {new_full_path}')

# Start processing from the root directory
remove_whitespace_from_filenames(root_directory)