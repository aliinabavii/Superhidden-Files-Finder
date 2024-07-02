import os

def list_superhidden_files(path):
    superhidden_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            attributes = os.stat(file_path).st_file_attributes
            if attributes & 4:  # Check if system attribute is set (bitwise AND with 4)
                superhidden_files.append(file_path)
    return superhidden_files

if __name__ == "__main__":
    path = "C:\\"  # Change this to the directory you want to search for superhidden files
    superhidden_files = list_superhidden_files(path)
    
    print("Superhidden Files:")
    for file_path in superhidden_files:
        print(file_path)