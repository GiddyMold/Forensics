import subprocess
import os

def collect_destination_folder_metadata(destination_path, debug):
    # Get the current directory where the script is run
    current_directory = os.getcwd()

    # Define the relative path to exiftool in the current directory based on current OS
    if os.name == 'nt':
        exiftool_path = os.path.join(current_directory, "exiftool.exe")
    elif os.name == 'posix':
        exiftool_path = os.path.join(current_directory, "Image-ExifTool/exiftool")

    # Create the command to execute exiftool on the target directory
    command = f'"{exiftool_path}" -a -r "{destination_path}" > "{current_directory}/metadata.txt"'

    try:
        # Execute the exiftool command and capture the output
        subprocess.check_output(command, shell=True, universal_newlines=True, stderr=subprocess.STDOUT)

    except subprocess.CalledProcessError as e:
        if debug:
            print(f"Error: {e}")
        else:
            pass
          
    if os.path.exists('metadata.txt'):
        print("Successfully created metadata.txt")
    else:
        print("Error creating metadata.txt file")
    
    if debug:
        with open('metadata.txt', 'r') as metadata_file:
            metadata_contents = metadata_file.read()
            print(metadata_contents)