# project_name , seq_name, shot_name, version, frame, path

import os
import csv
import re

path = '/home/rapa/project'

csv_path = os.path.expanduser('~/Project_AvaTop_data_v01.csv')


f_dict = {}
for r,d,f in os.walk(path):
    for fi in f:
        fp = os.path.join(r,fi)
        print(fp)
        dir_path = r
        #dir_path : /home/rapa/pro..../v001
        #fp : /home/rapa/pro..../v001/foo_0010....jpg
        if dir_path not in f_dict:
            f_dict[dir_path] = []
        # f_dict :{'/home/rapa...../v001' : []}
        f_dict[dir_path].append(fp)
# print(f_dict)


# reguler 정규표현방식
def get_info(path): 
    info = {
        "project" : None,
        "seq" : None,
        "shot" : None,
        "version" : None,
        "frame" : None,
        "path" : None

    }

    m = re.search('/home/rapa/project/(\w+)/shot/(\w+)/(\w+)/plate/(\w+)/.+', path)
    #print(m)

    if m:
        info["project"] = m.group(1)
        info["seq"] = m.group(2)
        info["shot"] = m.group(3)
        info["version"] = m.group(4)
        info["frame"] = m.group(4)
        info["path"] = m.group(4)
        
    return info

    print()



# if __name__ == "__main__":
#     print(get_project())
#     print(get_seq('avata'))
#     print(get_shot('avata', 'far'))
#     print(get_version('avata', 'far', '0010'))
    
#     print(get_path_info('/home/rapa/project/avata/shot/far/0010/plate/v001'))



def list_w(file_name):
    with open(csv_path, 'w') as f:
        writer = csv.writer(f)   # writer 저장도와주는놈
        writer.writerow([file_name])




if __name__ == "__main__":
    # print(get_project())
    # print(get_seq('avata'))
    # print(get_shot('avata','boo'))
    # print(get_version('avata','far','0010'))

    # print(get_project())
    # print(get_seq())
    # print(get_shot())


    



    #쓰기
    with open(csv_path, 'w') as f:
        w = csv.writer(f)   # writer 저장도와주는놈
        w.writerowh(get_info.project.keys())
        w.writerowh(get_info.project.value())
   
    
    