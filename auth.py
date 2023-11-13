# Import necessary modules
import os          # Provides access to operating system functions

def check_authenticity(source_path, destination_path, debug):
    error = False
    source_files = set()
    destination_files = set()

    # Collect file paths from the source folder tree
    for root, _, files in os.walk(source_path):
        for file in files:
            file_path = os.path.relpath(os.path.join(root, file), source_path)
            source_files.add(file_path)

    # Collect file paths from the destination folder tree
    for root, _, files in os.walk(destination_path):
        for file in files:
            file_path = os.path.relpath(os.path.join(root, file), destination_path)
            destination_files.add(file_path)

    # Check the authenticity of each file
    for file in source_files:
        if file in destination_files:
            source_file_path = os.path.join(source_path, file)
            destination_file_path = os.path.join(destination_path, file)

            source_mtime = os.path.getmtime(source_file_path)
            destination_mtime = os.path.getmtime(destination_file_path)

            if source_mtime == destination_mtime:
                if debug == True:
                    print("[✓] File Authenticity Maintained:", destination_file_path)
                pass
            else:
                print("[✕] File Authenticity NOT Maintained:", destination_file_path)
                error = True
        else:
            print("[✕] File Missing in Destination:", os.path.join(destination_path, file))
            error = True
    
    if error == False:
        print("Authenticity of all files is maintained")