# Import necessary modules
import os          # Provides access to operating system functions
import sys         # Provides access to additional system functions
import subprocess  # Provides access to subprocess functions
import tkinter as tk
from tkinter import filedialog
from GUI import return_GUI

debug = False
gui = False

def start():
    if len(sys.argv) > 1 and (sys.argv[1] == "--help" or sys.argv[1] == "-help" or sys.argv[1] == "-h" or sys.argv[1] == "--h"):
        print("""
    This script is designed to copy the entire contents of a specified source drive to a destination directory while preserving file integrity and collecting metadata. Additionally, it can set the source drive to read-only mode and remove the read-only attribute when necessary.

    Usage:
        python main.py [OPTIONS]

    Options:
    --help, -help, -h, --h                      Display this help message and exit.
    --version, -version, --v, -v                Display the version information and exit.
    --debug, -debug, --d, -d                    Enable debugging mode.
    --gui, -gui, --g, -g                        Enable graphical user interface (GUI) mode.
    --requirements, -requirements, --r, -r      Display the requirements and exit.

    Input:
        1. Source Drive Letter:
            - Enter the source drive letter (A-Z) when prompted. It represents the drive to be copied.

        2. Destination Path:
            - Enter the destination path where you want to copy the source drive's contents.
            - You can use both forward slashes (/) and backslashes (\) in the path.
            - For paths containing special characters, double the backslashes (\\\\).
            - The destination directory will be created if it doesn't exist.

    Example:
        [Terminal] python3 script_name.py
        [Prompt]   Enter the source drive letter (A-Z) or path to filesystem: D
        [Prompt]   Enter the destination path: C:\\\\Backup\\MyFiles

    Response:
        - The script will copy the contents of the specified source drive (D) to the destination directory (C:\Backup\MyFiles).
        - It will set the source drive (D) to read-only mode if not already in that state and then remove the read-only attribute after copying.
        - The script will compare file hashes to ensure data integrity during the copy process.
        - It will print the file tree of the destination directory and collect metadata in a 'metadata.txt' file.

    Troubleshooting:
        If you encounter issues or errors, consider the following:
        - Ensure the source drive exists.
        - Check if the destination path is properly formatted.
        - Verify that the required modules are installed.
        - Review the generated 'Results' folder and 'results.txt' file for detailed information.
        - The script may require administrative privileges to set the source drive to read-only mode.
        - Make sure that on Unix systems Image-ExifTool/exiftool has executable permissions.
        - Make sure to run this script with appropriate permissions to access the source drive and create files in the destination directory.
        - If you have trouble finding filesystem of your drive using linux system, use "df -h" command and provide information from first column.

    Disclaimer:
        - This script is designed for specific use cases and may not be suitable for general purposes. Use it with caution.
    """)
        exit()
    elif len(sys.argv) > 1 and (sys.argv[1] == "--version" or sys.argv[1] == "-version" or sys.argv[1] == "--v" or sys.argv[1] == "-v"):
        print("20230602 (4) Informatyka Śledcza - projekt 1")
        exit()
    elif len(sys.argv) > 1 and (sys.argv[1] == "--debug" or sys.argv[1] == "-debug" or sys.argv[1] == "--d" or sys.argv[1] == "-d"):
        global debug
        debug = True
    elif len(sys.argv) > 1 and (sys.argv[1] == "--gui" or sys.argv[1] == "-gui" or sys.argv[1] == "--g" or sys.argv[1] == "-g"):
        global gui
        gui = True
    elif len(sys.argv) > 1 and (sys.argv[1] == "--requierments" or sys.argv[1] == "-requierments" or sys.argv[1] == "--r" or sys.argv[1] == "-r"):
        try:
            subprocess.run(["pip", "install", "humanize", "psutil"], check=True)
            print("Packages installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")
        exit()
    elif len(sys.argv) > 1:
        print("""
        Unknown Option:
        
        The option you provided is not recognized. Please use one of the following valid options:

        1. For help and usage information:
        python3 script_name.py --help

        2. To check the script version:
        python3 script_name.py --version
              
        3. To debug the script:
        python3 script_name.py --debug
        """)
        exit()

def user_input():
    # Prompt the user for source drive and destination path
    global gui
    if gui == True:
        name, source_drive, first_copy, destination_path = return_GUI()
    else:
        name = input("Enter your full name: ")
        source_drive = input("Enter the source drive letter (A-Z) or path to filesystem: ").upper()
        first_copy = input("Enter the destination path of first copy: ")
        destination_path = input("Enter the destination path of second copy: ")

    if not name:                                                              # Default paths for fast debbugging
        name = "Debug"                                                        # Default paths for fast debbugging
    if not source_drive:                                                      # Default paths for fast debbugging
        if os.name == 'posix':  # Unix system                                 # Default paths for fast debbugging
            source_drive = '/dev/sr0'                                         # Default paths for fast debbugging
        elif os.name == 'nt':  # Windows system                               # Default paths for fast debbugging
            source_drive = "D"                                                # Default paths for fast debbugging
    if not first_copy:                                                        # Default paths for fast debbugging
        first_copy = os.path.join(os.getcwd(), "First_Copy")                  # Default paths for fast debbugging  
    if not destination_path:                                                  # Default paths for fast debbugging
        destination_path = os.path.join(os.getcwd(), "Second_Copy")           # Default paths for fast debbugging

    # Ensure the destination path is properly formatted
    first_copy = first_copy.replace("\\","/")
    destination_path = destination_path.replace("\\", "/")

    # Form the source path using the provided source drive letter OR assign source path in case of Unix systems
    if len(source_drive) == 1:
        source_path = f"{source_drive}:\\"
    else:
        source_path = source_drive

    # Check if the source drive exists
    if not os.path.exists(f"{source_path}"):
        print(f"The source drive {source_drive} does not exist.")
        exit()
        
    # Check if the destination directory exists
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)

    return name, source_path, source_drive, first_copy, destination_path

def is_debug():
    return debug

def interval():
    print("\n▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇\n")