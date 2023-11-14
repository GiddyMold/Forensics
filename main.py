# Import necessary modules
import os          # Provides access to operating system functions
import sys         # Provides access to additional system functions
import shutil      # Helps with file operations
import hashlib     # Provides cryptographic hash functions
import time        # Import time module
from datetime import datetime
from hash import hash
from interface import start, user_input, interval, is_debug
from tree import print_file_tree
from read_only import execute_read_only, remove_drive_read_only
from copy_drive import copy, is_unix
from auth import check_authenticity
from metadata import collect_destination_folder_metadata
from results import create_results
from drive_info import get_drive_parameters, get_filesystem_info

def record_time():
    interval()
    start()
    name, source_path, source_drive, first_copy, destination_path = user_input()
    interval()
    
    start_time = datetime.now()  # Record the start time using the current system time

    # Get information about the file system of the source drive
    get_filesystem_info(source_path, source_drive)
    interval()
    
    # Get drive information and parameters
    drive_parameters = get_drive_parameters(source_path, is_debug())

    # Set the file to read-only mode
    execute_read_only(source_drive, source_path)
    interval()

    # Copy the source drive and check for integrity & authenticity
    source_path = is_unix(source_path)  # Assign different source path in case of Unix systems
    copy(first_copy, source_path)  # Make copy number 1 of the source drive
    hash1 = hash(source_path, first_copy, is_debug())  # Compare file hashes \ Checks integrity of files
    check_authenticity(source_path, first_copy, is_debug())  # Checks authenticity of files
    interval()

    # Duplicate the existing copy and check for integrity & authenticity
    copy(destination_path, first_copy)  # Make copy number 2 of the source drive
    hash2 = hash(first_copy, destination_path, is_debug())  # Compare file hashes \ Checks integrity of files
    check_authenticity(first_copy, destination_path, is_debug())  # Checks authenticity of files
    interval()

    # Print the file tree and metadata of the destination directory
    print("File Tree of the Destination Directory:")
    print_file_tree(destination_path)
    interval()

    # Execute the function to check and collect metadata
    collect_destination_folder_metadata(destination_path, is_debug())
    interval()

    # Remove the read-only attribute from the D: drive and check if the D: drive is in READ-ONLY mode after removing the attribute
    remove_drive_read_only(source_drive, source_drive)
    interval()
    
    end_time = datetime.now()  # Record the end time using the current system time
    
    # Create results folder and file within
    create_results(name, drive_parameters, source_drive, first_copy, destination_path, hash1, hash2, start_time, end_time, is_debug())
    interval()

    # Print timestamps of running the program
    print(f"Start Time: {start_time}")
    print(f"End Time: {end_time}")
    print(f"Running Time: {end_time - start_time}")
    interval()
    
if __name__ == "__main__":
    record_time()