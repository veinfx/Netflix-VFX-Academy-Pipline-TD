import os
path = '/home/rapa/project'

f_dict = {}
for r,d,f in os.walk(path):
    for fi in f:
        fp = os.path.join(r,fi)
        # print(fp)
        dir_path = r
        #dir_path : /home/rapa/pro..../v001
        #fp : /home/rapa/pro..../v001/foo_0010....jpg
        if dir_path not in f_dict:
            f_dict[dir_path] = []
        # f_dict :{'/home/rapa...../v001' : []}
        f_dict[dir_path].append(fp)
print(f_dict)


#상위 디렉토리 그룹핑 