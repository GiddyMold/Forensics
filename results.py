import os

def move_metadata_file():
    current_dir = os.getcwd()  # Get the current directory path
    source_file = os.path.join(current_dir, "metadata.txt")  # Path to the source file
    destination_folder = os.path.join(current_dir, "Results")  # Path to the destination folder
    
    if os.path.exists(source_file):
        if not os.path.exists(destination_folder):
            os.mkdir(destination_folder)  # Create the "Results" folder if it doesn't exist
        destination_file = os.path.join(destination_folder, "metadata.txt")  # Path to the destination file
        os.rename(source_file, destination_file)  # Move the file to the "Results" folder
    else:
        print("ERROR: File 'metadata.txt' not found in the current directory. File not moved.")

def create_results(name, drive_parameters, source_drive, first_copy, destination_path, hash1, hash2, start_time, end_time):
    # Create a "Results" folder in the current directory if it doesn't exist
    if not os.path.exists("Results"):
        os.mkdir("Results")

    # Define the file path for the results.txt file
    file_path = os.path.join("Results", "results.txt")
    
    #Move the metadata file
    move_metadata_file()

    # Open the results.txt file in append mode to add the variables' values
    with open(file_path, "a") as results_file:
        results_file.write(f"Auditor full name: {name}\n")
        for param in drive_parameters:
            results_file.write(f"{param}\n")
        results_file.write(f"Source Drive: {source_drive}\n")
        results_file.write(f"First Copy Destination Path: {first_copy}\n")
        results_file.write(f"Second Copy Destination Path: {destination_path}\n")
        results_file.write(f"Start Time: {start_time}\n")
        results_file.write(f"End Time: {end_time}\n")
        results_file.write(f"Running Time: {end_time - start_time} seconds\n")
        
        results_file.write("\nHashes of the files in the first copy:\n")
        for file_dict in hash1:
            for file_path, file_hash in file_dict.items():
                results_file.write(f"{file_path}: {file_hash}\n")
        
        results_file.write("\nHashes of the files in the second copy:\n")
        for file_dict in hash2:
            for file_path, file_hash in file_dict.items():
                results_file.write(f"{file_path}: {file_hash}\n")

            
    print("'Results' folder & results.txt creation successfull.")