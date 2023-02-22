# foo > far

import os

path = '/home/rapa/project'
# dirlist = os.listdir(path)

# print(dirlist)


def DirCheck(path):
    file_list = os.listdir(path)
    for name in file_list:
        new_path = os.path.join(path.name)
        #print("path" + new_path)
        if os.path.isdir(new_path):
            print(name + ":폴더")
            Rename(name,new_path, path)
        elif os.path.isdir(new_path):
            print("폴더 시작")
            DirCheck(new_path)
            print("폴더 확인")
        else:
            print(name + ": 아무것도아님")

def Rename(name, before_path, after_path):
    old_name = "foo"
    new_name = str(name)
    new_name = new_name.replace(old_name,"")
    os.rename(before_path, after_path + "/" + new_name)
    print(new_name)

DirCheck(path)