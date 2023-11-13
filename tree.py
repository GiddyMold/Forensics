# Import necessary modules
import os          # Provides access to operating system functions

def print_file_tree(directory, indent=""):
    items = os.listdir(directory)                                   # Get a list of items (files and subdirectories) in the specified directory and subdirectories
    items.sort()                                                    # Sort the items for consistent output
    for i, item in enumerate(items):                                # Iterate through the items in the directory
        item_path = os.path.join(directory, item)                   # Construct the full path of the item
        is_last = (i == len(items) - 1)                             # Check if this is the last item in the list
        if os.path.isdir(item_path):                                # If the item is a directory, print its name with a '└──' or '├──' marker
            print(indent + "└── " + item + os.path.sep)             # Print directory name
            new_indent = indent + ("    " if is_last else "│   ")   # Create a new indentation for the subdirectory
            print_file_tree(item_path, new_indent)                  # Recursively call the function to print the subdirectory's contents
        else:                                                       # If the item is a file, print its name with a '└──' or '├──' marker
            print(indent + ("└── " if is_last else "├── ") + item)  # Print file name