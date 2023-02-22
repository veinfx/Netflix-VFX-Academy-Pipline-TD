import os

path_dir = '/home/rapa/project'
#path_dir_seq = '/home/rapa/project/avata/shot' 
#path_dir_shot = '/home/rapa/project/avata/shot/foo'


def get_project():
    project_list = os.listdir(path_dir)
    return project_list
    

def get_seq(project_name):
    seq_list = os.listdir(path_dir_seq)
    return seq_list
    

def get_shot():
    shot_list = os.listdir(path_dir_shot)
    return shot_list
    

def get_path_info(path_dir):
    path_info = os.listdir(path_dir)
    return path_info



if __name__ == "__main__":

    print("프로젝트 리스트:", get_project())
    print("시퀀스 리스트:", get_seq())
    print("샷 리스트:", get_shot())
    print("모든 경로", path_info())
    

    