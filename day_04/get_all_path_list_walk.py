import os
#os.walk


if __name__ == "__main__":
    path_dir = "/home/rapa/project"

    for (path, dirs, files) in os.walk(path_dir):
        print('# path :' + path)
        if len(dirs) > 0:
            for dir_name in dirs:
                print("dir: " + dir_name)
        
        if len(files) > 0:
            for file_name in files:
                print("file: " + file_name)



