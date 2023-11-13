# Import necessary modules
import os          # Provides access to operating system functions
import shutil      # Helps with file operations
import subprocess  # Allows for system commands to be executed

def copy(destination_path,source_path):
    # Ensure the destination directory exists
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)  # Create the destination directory if it doesn't exist

    # Copy the entire contents of the D: drive to the destination
    for root, dirs, files in os.walk(source_path):
        destination_dir = os.path.join(destination_path, os.path.relpath(root, source_path))
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)
        for file in files:
            source_file = os.path.join(root, file)
            destination_file = os.path.join(destination_dir, file)
            shutil.copy2(source_file, destination_file)  # Copy files from source to destination preserving metadata
            
def is_unix(source_path):
    if os.name == 'posix':
        try:
            # Run the df -h command and capture the output
            df_output = subprocess.check_output(['df', '-h']).decode('utf-8')

            # Split the output into lines
            lines = df_output.split('\n')

            # Iterate through lines to find the matching source_path
            for line in lines[1:]:
                # Skip empty lines
                if not line:
                    continue

                # Split the line into columns
                columns = line.split()

                # Check if the source_path matches the input
                if columns[0] == source_path:
                    # Return the "mounted on" value
                    return columns[-1]

            # If the source_path is not found
            return f"source_path '{source_path}' not found in df -h output."

        except subprocess.CalledProcessError as e:
            # Handle any errors that may occur during the subprocess call
            return f"Error: {e}"
    else:
        return source_path