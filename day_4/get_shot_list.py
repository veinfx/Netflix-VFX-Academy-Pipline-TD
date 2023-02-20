import os

path_avata_shot_foo = '/home/rapa/project/avata/shot/foo'
path_avata_shot_boo = '/home/rapa/project/avata/shot/boo'


path_topgun_shot_foo = '/home/rapa/project/topgun/shot/foo'
path_topgun_shot_boo = '/home/rapa/project/topgun/shot/boo'


avata_shot_foo_list = os.listdir(path_avata_shot_foo)
avata_shot_boo_list = os.listdir(path_avata_shot_boo)

topgun_shot_foo_list = os.listdir(path_topgun_shot_foo)
topgun_shot_boo_list = os.listdir(path_topgun_shot_boo)


print("아바타 foo 샷 리스트",avata_shot_foo_list)
print("아바타 boo 샷 리스트",avata_shot_boo_list)


print("탑건 foo 샷 리스트",topgun_shot_foo_list)
print("탑건 boo 샷 리스트",topgun_shot_boo_list)