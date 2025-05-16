import os
import shutil

# Ask the user for the source and destination directory
source_dir = input("Please enter the path to the source directory: ")
destination_dir = input("Please enter the path to the destination directory: ")

# Confirm the directories with the user before proceeding
print(f"Source directory: {source_dir}")
print(f"Destination directory: {destination_dir}")
confirmation = input("Is this correct? (yes/no): ")

if confirmation.lower() == 'yes':
    # Walk through all subdirectories in the source directory
    for dirpath, dirnames, files in os.walk(source_dir):
        for file in files:
            # Construct the full file path
            file_path = os.path.join(dirpath, file)
            # Define new destination path
            dest_file_path = os.path.join(destination_dir, file)
            # Move each file to the destination directory
            shutil.move(file_path, dest_file_path)

    print("Files moved successfully!")
else:
    print("Operation cancelled.")
