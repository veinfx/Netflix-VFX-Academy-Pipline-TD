import os

dir_path = '/home/rapa/psw/'

# os.makedirs(dir_path)
# os.rmdir(dir_path)


if not os.path.exists(dir_path):
    os.makedirs(dir_path)
else:
    print("Exist.")