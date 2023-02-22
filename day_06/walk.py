import os

path = "/home/rapa/project"

for path, dirs, files in os.walk(path):
    print("-"*30)
    print(path)
    print("-"*30)
    print(dirs)
    print("-"*30)
    print(files)
   