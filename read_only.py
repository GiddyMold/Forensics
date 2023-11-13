# Import necessary modules
import os          # Provides access to operating system functions
import subprocess

# Function to set a drive to read-only
def set_drive_read_only(drive_letter, source_path):
    if os.name == 'posix':  # Unix system
        command = f"chmod -R a-w {source_path}"
        subprocess.run(command, shell=True)
    elif os.name == 'nt':  # Windows system
        os.system(f"attrib +R {drive_letter}: > nul 2>&1")
    else:
        print("Unsupported operating system")

# Function to remove read-only attribute from a drive
def remove_drive_read_only(drive_letter, source_drive):
    if os.name == 'posix':
        command = f"chmod -R +w {source_drive}"
        subprocess.run(command, shell=True)
        if is_drive_read_only(source_drive):
            print(f"{source_drive}: Removing READ-ONLY mode failed. Drive is still in READ-ONLY mode.")
        else:
            print(f"{source_drive}: Removing READ-ONLY mode successful. Drive is in READ-WRITE mode now.")
    elif os.name == 'nt':
        os.system(f"attrib -R {drive_letter}: > nul 2>&1")  # Removes the read-only attribute from the drive
        if is_drive_read_only(source_drive):
            print(f"{source_drive}: Removing READ-ONLY mode failed. Drive is still in READ-ONLY mode.")
        else:
            print(f"{source_drive}: Removing READ-ONLY mode successful. Drive is in READ-WRITE mode now.")
    else:
        print("Unsupported operating system")

# Function to check if a drive is in read-only mode
def is_drive_read_only(source_path):
    try:
        # Try to create a temporary file on the drive to check if it's read-only
        temp_dir = f"{source_path}temp_check_read_only"
        os.makedirs(temp_dir, exist_ok=True)
        with open(os.path.join(temp_dir, "temp_file.txt"), "w") as file:
            file.write("Test content")
        os.remove(os.path.join(temp_dir, "temp_file.txt"))
        os.rmdir(temp_dir)
        return False  # Drive is not read-only
    except PermissionError:
        return True  # Drive is in read-only mode

def execute_read_only(source_drive, source_path):
    # Check if the D: drive is in READ-ONLY mode before setting it
    if is_drive_read_only(source_path):
        print(source_drive,": drive is already in READ-ONLY mode.",sep="")  # Print a message if the drive is already in read-only mode
    else:
        # Set the D: drive to read-only
        set_drive_read_only(source_drive, source_path)
        print(source_drive,": drive is now in READ-ONLY mode.",sep="")  # Print a message after setting the drive to read-only