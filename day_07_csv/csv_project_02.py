# project_name , seq_name, shot_name, version, frame, path

# avata foo 0010 v001 10 /home/rapa.../foo_0010_plate_v001.###.jpg

import os
import csv

path = '/home/rapa/project/'

csv_path = os.path.expanduser('~/Project_AvaTop_data.csv')


for roots,dirs, files in os.walk(path):
    # for dir in dirs:
    #     # print(roots,dir)
    #     if dir == "bar":
    #         path = os.path.join(roots,dir)
    #         print(path)
    for file_name in files:
        if file_name.endswith(".jpg"):
            path = os.path.join(roots,file_name)
            split = path.split(os.sep)
            del split[0]
            print(split)
            # print(roots)
          
            # print(dirs)
           
            # print(files)
       

            # print(file_name)
            # print(path)
        
            # with open(csv_path, 'w') as f:
            #     writer = csv.writer(f)   # writer 저장도와주는놈
            #     writer.writerow([file_name])

            