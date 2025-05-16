# file_mover
Simple Python script for moving files between directories

🗂️ File Mover Script
A simple Python script that moves files from one directory to another, including all files inside nested subdirectories. Useful for organizing scattered files into a single location.

🚀 Features
Prompts the user for the source and destination directory paths

Walks through all subfolders in the source directory

Moves all files (ignoring folder structure) into the destination directory

Prevents accidental moves by requiring user confirmation

📁 How It Works
This script uses os.walk() to recursively loop through all subdirectories of the source folder. It then moves each file to the specified destination using shutil.move().

Note: Folder structure is not preserved — all files are moved flat into the destination.

🛠️ Requirements
Python 3.x

🧑‍💻 Usage
Run the script:

bash
Copy
Edit
python file_mover.py
Enter the full path to:

The source directory

The destination directory

Confirm the paths when prompted.

The script will recursively move all files.

📝 Example
If your source_dir contains:

css
Copy
Edit
source_dir/
├── a.txt
├── sub1/
│   └── b.txt
└── sub2/
    └── c.txt
And your destination_dir is empty, after running the script:

css
Copy
Edit
destination_dir/
├── a.txt
├── b.txt
└── c.txt
⚠️ Notes
Files with the same name will overwrite each other in the destination folder.

This script does not copy — it removes files from the source.

Run it only after backing up important data.

📬 Contributions
Feel free to open issues or fork the repo to improve the script!
