import os

path = '/home/rapa/project/'

for roots, dirs, files in os.walk(path):
    # print(roots)
    # # print("--" * 30)
    # print(dirs)
    # # print("--" * 30)
    # # print(files)
    # # print("--" * 30)

    # for dir in dirs:
    #     #print(dir)
    #     #print(dirs) # 리스트로 나옴
        # if dir == "bar":
        #     get_path = os.path.join(roots,dir)
        #     print(get_path)
    
    for file_name in files:
        if file_name.endswith(".jpg"):
            get_path = os.path.join(roots,file_name)
            print(get_path)
    
    