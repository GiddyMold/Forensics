# Import necessary modules
import hashlib     # Provides cryptographic hash functions
import os

# Function to calculate SHA-512 hash for a file
def get_file_hash_sha512(file_path):
    hasher = hashlib.sha512()  # Create a SHA-512 hash object
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(8192)  # Read the file in 8KB chunks
            if not data:
                break
            hasher.update(data)  # Update the hash with the read data
    return hasher.hexdigest()  # Return the hexadecimal digest of the hash

# Function to compare hashes and check file integrity
def compare_file_hashes(source_file, destination_file, debug):
    source_hash = get_file_hash_sha512(source_file)  # Get the SHA-512 hash of the source file
    destination_hash = get_file_hash_sha512(destination_file)  # Get the SHA-512 hash of the destination file
    if source_hash == destination_hash:
        if debug:
            print("[✓] File Integrity Maintained:", destination_file)  # Print if file integrity is maintained
            print("Hash of source file:", source_hash)  # Print the hash of the source file
            print("Hash of destination file:", destination_hash)  # Print the hash of the destination file
        return source_hash  # Return the hash value as a result
    else:
        print("[✕] File Integrity NOT Maintained:", destination_file)  # Print if file integrity is not maintained
        return None  # Error detected

# Compare hashes for each file and return a list of hashes
def hash(source_path, destination_path, debug):
    hash_list = []
    for root, _, files in os.walk(source_path):
        for file in files:
            source_file = os.path.join(root, file)
            relative_path = os.path.relpath(source_file, source_path)
            destination_file = os.path.join(destination_path, relative_path)
            hash_value = compare_file_hashes(source_file, destination_file, debug)
            if hash_value is not None:  # Check if the comparison was successful
                hash_list.append({destination_file: hash_value})
    if len(hash_list) == 0:
        print("No files with matching integrity found.")
    else:
        print("Integrity of all matching files is maintained.")
    return hash_list