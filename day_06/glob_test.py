import glob
import os

##1

# path = '/home/rapa/project/avata/shot/far/0010/plate'
# file_list = glob(path + "/*.jpg")
# print(file_list)

##2

# file_list = glob.glob('/home/rapa/project/**/far_*.jpg', recursive=True)

# print(file_list)


##3

for roots,dirs, files in os.walk('/home/rapa/project'):
    # print(dirs)  ## >> 리스트로 나옴!
    # for dir in dirs:
    #     # print(roots,dir)
    #     print(dir)

    # #     if dir == "bar":
    #         path = os.path.join(roots,dir)
    #         print(path)

    for file_name in files:
       
        if file_name.endswith(".jpg"):
             # startswith : 시작하는문자, 시작지점 , endswith : 끝나는문자, 문자열의시작, 문자열의끝
            
            path = os.path.join(roots,file_name)
            print(path)