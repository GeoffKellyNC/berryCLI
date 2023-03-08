import os
import subprocess



def delete_files_in_folders():
    file_locations = ['/Users/geoff/Downloads']
    for file_location in file_locations:
        if os.path.exists(file_location):
            for filename in os.listdir(file_location):
                file_path = os.path.join(file_location, filename)
                try:
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                        print(f"Deleted {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")
        else:
            print(f"{file_location} does not exist")
    subprocess.run(['osascript', '-e', 'tell app "Finder" to empty trash'])
    return