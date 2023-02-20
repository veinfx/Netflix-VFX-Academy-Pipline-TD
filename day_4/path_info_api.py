import os
import re

project_path = "/home/rapa/project"

def get_project():
    project_list = os.listdir(project_path)
    return project_list

def get_seq(project_name):
    seq_path = project_path + os.sep + project_name + os.sep + "shot"
    seq_list = os.listdir(seq_path)
    return seq_list

def get_shot(project_name, seq_name):
    shot_path = project_path + os.sep + project_name + os.sep + "shot" + os.sep + seq_name
    shot_list = os.listdir(shot_path)
    return shot_list


# reguler 정규표현방식
def get_path_info(project_path): 
    info = {
        "project" : None,
        "seq" : None,
        "shot" : None
    }
    # p = re.compile('/home/rapa/project/(\w+)/shot/(\w+)/(\w+)/.+')
    # m = p.search(path)

    m = re.search('/home/rapa/project/(\w+)/shot/(\w+)/(\w+)/.+', project_path)
    #print(m)

    if m:
        info["project"] = m.group(1)
        info["seq"] = m.group(2)
        info["shot"] = m.group(3)
    return info


# split 비추 경로없으면 에러 > 에러 방지추가할것

"""
def get_path_info2(path):
    path_split = path.split("/")
    project_name = path_split[4]
    seq_name = path_split[6]
    shot_name = path_split[7]
    return project_name, seq_name, shot_name
"""

if __name__ == "__main__":
    print(get_project())
    print(get_seq('avata'))
    print(get_shot('avata', 'foo'))
    print(get_path_info('/home/rapa/project/avata/shot/foo/0010/plate/v001'))



  #  print(get_path_info2('/home/rapa/project/avata/shot/foo/0010/plate/v001'))