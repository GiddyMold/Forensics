import psutil
import humanize

drive_parameters = []

def get_drive_parameters(source_path, debug):
    # Get the disk partitions
    partitions = psutil.disk_partitions()

    # Iterate through the partitions
    for partition in partitions:
        if partition.device == source_path:
            # Get the usage statistics of the partition
            usage = psutil.disk_usage(partition.mountpoint)
            drive_parameters.append(f"Drive exact path: {partition.device}")
            drive_parameters.append(f"Mountpoint path: {partition.mountpoint}")
            drive_parameters.append(f"File system type: {partition.fstype}")
            drive_parameters.append(f"Total size: {humanize.naturalsize(usage.total)}")
            drive_parameters.append(f"Used space: {humanize.naturalsize(usage.used)}")
            drive_parameters.append(f"Free space: {humanize.naturalsize(usage.free)}")
            drive_parameters.append(f"Usage percentage: {usage.percent}%")
            drive_parameters.append(f"Options: {partition.opts}")
            drive_parameters.append(f"Max file descriptors: {partition.maxfile}")
            drive_parameters.append(f"Max filename length: {partition.maxpath}")
            
            if debug == True:
                print("Drive information:")
                print(f"Drive exact path: {partition.device}")
                print(f"Mountpoint path: {partition.mountpoint}")
                print(f"File system type: {partition.fstype}")
                print(f"Total size: {humanize.naturalsize(usage.total)}")
                print(f"Used space: {humanize.naturalsize(usage.used)}")
                print(f"Free space: {humanize.naturalsize(usage.free)}")
                print(f"Usage percentage: {usage.percent}%")
                print(f"Options: {partition.opts}")
                print(f"Max file descriptors: {partition.maxfile}")
                print(f"Max filename length: {partition.maxpath}")
            
            break
        
    return drive_parameters


# Function to get file system information
def get_filesystem_info(source_path, drive_letter):
    try:
        partitions = psutil.disk_partitions()
        for partition in partitions:
            if partition.device == source_path:
                command = partition.fstype      # Command to get file system type using psutil library
                print("File System of ", drive_letter,": ",command,sep="")
                return None
    except Exception as e:
        print("Error:", e)  # Print an error message if there's an exception
        return None
    print("File System of ", drive_letter,": Unknown",sep="")  # Print "Unknown" if unable to determine filesystem