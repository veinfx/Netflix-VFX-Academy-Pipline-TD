import gazu


class HooChu():
    def __init__(self):
        gazu.client.set_host("http://192.168.3.116/api")
        gazu.log_in("pipeline@rapa.org", "netflixacademy")

        self._name = ''
        self._new_proj = ''
        # self._project = ''
        self._new_assets = ''

        pass

    @property
    def name(self):
        """
        type : string , 프로젝트 이름
        """
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def new_proj(self):
        """
        new_proj : 새로운프로젝트 path  == id
        """
        return self._new_proj

    @new_proj.setter
    def new_proj(self, value):
        self._new_proj = value

    @property
    def new_assets(self):
        """
        new_assets : 새로운 에셋
        """
        return self._new_assets

    @new_assets.setter
    def new_assets(self, value):
        self._new_assets = value

    def all_proj(self):
        """
        오픈된 프로젝트들
        """
        all_proj = gazu.project.all_open_projects()
        return all_proj

    def new_project(self):
        """
        새로운 프로젝트 생성,
        """
        self.new_proj = gazu.project.new_project(self._name)

    def get_project(self):
        """
        get project by name
        """
        self._get_project = gazu.project.get_project_by_name(self._name)
        return self._get_project

    def close_project(self):
        """
        프로젝트 비활성화
        """
        gazu.project.close_project(self._get_project)

    def remove_project(self):
        """
        프로젝트 삭제
        """
        gazu.project.remove_project(self._get_project)

    '''
    def edit_project
    def 

    '''
    def new_assets(self):
        # self.all_assets = gazu.asset.all_assets_for_project(self.new_project())
        # self._new_asset = gazu.asset.new_asset(self.new_project(),'asset_type'',"asset_test")
        # asset = gazu.asset.new_asset(
        #     project_dict,
        #     asset_type_dict,
        #     "My new asset",
        #     "My asset description"
        # )
        self._new_assets = gazu.asset.new_asset(self.new_project(), "S1")
        return self._new_assets
        # gazu.shot.new_sequence("0249b2ef-5252-4db6-b22e-72082cfca24d", "S1_01_06")


def main():
    a = HooChu()
    a.name = "avata3"
    # a.all_proj()

    # a.new_project()
    a.get_project()
    prodict = a.get_project()
    # a.close_project()
    # a.remove_project()

    asset_types = gazu.asset.all_asset_types()
    # print(asset_types)

    asset_type = gazu.asset.new_asset_type("my new asset_type") #에셋 타입추가

    # asset_types = gazu.asset.all_asset_types_for_project(a.new_project())
    asset = gazu.asset.new_asset(prodict,asset_type,"cam1")
    # print(asset)

    # print(a.all_proj())
    # print(a.get_project())
    # print(a.get_project())
    # a.new_assets()
    # print(a.asset_tset())
    # asset = gazu.asset.new_asset(
    #     a.name,
    #     a.name,
    #     "My new asset",
    #     "My asset description"
    # )

    # asset = gazu.asset.update_asset(new_values_dict)
    # gazu.asset.remove_asset(asset)

if __name__ == "__main__":
    main()

    # all_proj = gazu.project.all_projects()
    # print(all_proj)
    # for i in all_proj:
    # print(i)

# 새로운 프로젝트 생성
# project = gazu.project.new_project("avata3")
# print(project)


# project = gazu.project.get_project_by_name("avata3")
# # gazu.project.close_project(project)
# # gazu.project.remove_project(project)
# print(project)


# project post
# projects = gazu.client.post("data/projects", {"name": "avata3"})
# print(projects)

# a = gazu.client.get("data/project")
#
# for i in a:
#     print(i)
# gazu.project.all_open_projects()
# print(project)

# for i in all_proj:
#     print(i)
# gazu.project.close_project(project)
# gazu.client.delete(445925d0-8259-4e14-b2ce-72bc9b9ec1c9")


# persons = gazu.person.all_persons()
# print(persons)

# gazu.client.get("data/projects")
# gazu.client.delete("data/projects/8ae35259-d325-4af2-beed-26992d7c6f7d")

# assets = gazu.asset.all_assets_for_project(project_dict)
# assets = gazu.asset.all_assets_for_shot(shot_dict)
# assets = gazu.asset.all_assets_for_project_and_type(project_dict, asset_type_dict)
#
# asset = gazu.asset.new_asset(
#     project_dict,
#     asset_type_dict,
#     "My new asset",
#     "My asset description"
# )
