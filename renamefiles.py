import os

def rename_files(directory):
    # List all files in the directory
    files = os.listdir(directory)

    for filename in files:
        # Check if the file is a regular file
        if os.path.isfile(os.path.join(directory, filename)):
            # Strip "Memoji" from the filename
            new_filename = filename.replace("Memoji", "")
            
            # Rename the file
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            print(f"Renamed {filename} to {new_filename}")

# Specify the directory path
directory_path = "./avatars"

# Call the function to rename files in the directory
rename_files(directory_path)
