import os

def print_files_in_dir(path_dir, prefix):
    files = os.listdir(path_dir)
    for file in files:
        path = os.path.join(path_dir,file)
        print(prefix + path)

if __name__ == "__main__":
    path_dir = "/home/rapa/project"
    print_files_dir(path_dir,"")