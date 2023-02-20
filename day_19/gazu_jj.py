import gazu
gazu.client.set_host("http://192.168.3.116/api")
gazu.log_in("pipeline@rapa.org", "netflixacademy")
projects = gazu.client.post("data/projects", {"name": "Chopsticks"})
print(projects)
project = gazu.project.get_project_by_name("Chopsticks")
gazu.project.close_project(project)
gazu.client.delete(project)
a = gazu.client.get("data/projects")
for i in a:
    print(i)
gazu.project.add_metadata_descriptor("data/projects/0249b2ef-5252-4db6-b22e-72082cfca24d", "cut", "shot")
project = gazu.project.get_project_by_name("Chopsticks")
assets = gazu.asset.all_assets_for_project(project)
print(assets)
print(project)
gazu.shot.new_episode("0249b2ef-5252-4db6-b22e-72082cfca24d", "S1")
gazu.shot.new_sequence("0249b2ef-5252-4db6-b22e-72082cfca24d", "S1_01_06")
ptt = gazu.shot.get_sequence_by_name("0249b2ef-5252-4db6-b22e-72082cfca24d", "S1")
print(ptt)
gazu.shot.new_shot("0249b2ef-5252-4db6-b22e-72082cfca24d", "43f0905c-e01c-4645-949d-11ecf32f4c71", "S1_01",
nb_frames=151, frame_in=1, frame_out=151)