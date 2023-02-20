import os

path_avata_seq = '/home/rapa/project/avata/shot'
path_topgun_seq = '/home/rapa/project/topgun/shot'

avata_seq_list = os.listdir(path_avata_seq)
topgun_seq_list = os.listdir(path_topgun_seq)

print("아바타 시퀀스 리스트",avata_seq_list)
print("탑건 시퀀스 리스트",topgun_seq_list)