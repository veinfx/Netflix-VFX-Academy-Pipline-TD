import os
import re

# project path
path= '/home/rapa/project'

def get_project():
    project_list = os.listdir(path)
    return project_list
    

def get_seq(project_name):
    seq_path = path + os.sep + project_name + os.sep + "shot"
    seq_list = os.listdir(seq_path)
    return seq_list
    

def get_shot(project_name, seq_name):
    shot_path = path + os.sep + project_name + os.sep + "shot" + os.sep + seq_name
    shot_list = os.listdir(shot_path)
    return shot_list
    



# reguler 정규표현방식

def get_path_info(path):
    info = {
        "project" : None,
        "seq" : None,
        "shot" : None
    }

    m = re.search("/home/rapa/project/(\w+)/shot/(\w+)/(\w+)/plate/.+",path)
    #print(m)

    if m:
        info["project"] = m.group(1)
        info["seq"] = m.group(2)
        info["shot"] = m.group(3)
    return info



if __name__ == "__main__":

    print("프로젝트 리스트:", get_project())

    print("{} 의 시퀀스 리스트 :{} ".format("topgun",get_seq("topgun")))

    print("avata, foo 샷 리스트 : "), print(get_shot("avata","foo")) # 샷 리스트

    print(get_path_info("/home/rapa/project/topgun/shot/foo/0050/plate/v001"))

    print(get_path_info('/home/rapa/project/avata/shot/foo/0010/plate/v001'))
    

    