import gazu
import os

gazu.client.set_host("http://192.168.3.116/api")
gazu.log_in("pipeline@rapa.org", "netflixacademy")
hook = gazu.project.get_project_by_name("hook")
avata3 = gazu.project.get_project_by_name("Pizza")
chopsticks = gazu.project.get_project_by_name("chopsticks")
place = gazu.asset.get_asset_type_by_name("place")
# gazu.asset.new_asset(chopsticks, place, "daughters_room")
assets = (gazu.asset.all_assets_for_project(chopsticks))
shots = gazu.shot.all_shots_for_project(chopsticks)



tree_sample = {
    "working": {
        "mountpoint": "/your_mount_directory",
        "root": "your_root_directory",
        "folder_path": {
            "shot": "<Project>/shots/<Sequence>/<Shot>/<TaskType>",
            "asset": "<Project>/assets/<AssetType>/<Asset>/<TaskType>",
            "style": "lowercase"
},
        "file_name": {
            "shot": "<Project><Sequence><Shot><TaskType>",
            "asset": "<Project><AssetType><Asset><TaskType>",
            "style": "lowercase"
        }
    }
}

gazu.files.update_project_file_tree(your_project_name, tree_sample)
for shot in gazu.shot.all_shots_for_project(your_project_name):
    for task in gazu.task.all_tasks_for_shot(shot):
        path = os.path.dirname(
            gazu.files.build_working_file_path(task)[1:]
        )
        print(path)
        os.makedirs(os.sep + path)
for asset in gazu.asset.all_assets_for_project(your_project_name):
    for task in gazu.task.all_tasks_for_asset(asset):
        path = os.path.dirname(
            gazu.files.build_working_file_path(task)[1:]
        )
        print(path)
        os.makedirs(os.sep + path)