from pprint import pprint

import gazu


class HouChu:
    gazu.client.set_host("http://192.168.3.116/api")
    gazu.log_in("pipeline@rapa.org", "netflixacademy")

    def __init__(self):
        self._proj_name = None
        self._asset_name = None
        self._asset_type = None
    """
    getter , setter 
    """

    @property
    def proj_name(self):
        """
        type : string , 프로젝트 이름
        """
        return self._proj_name

    @proj_name.setter
    def proj_name(self, value):
        if type(value) == str:
            self._proj_name = value
        else:
            return None, "Need project"

    # @proj_name.setter
    # def proj_name(self, value):
    #     if type(value) == str:
    #         project = gazu.project.get_project_by_name(value)
    #         self._proj_name = project
    #         print(project)
    #     else:
    #         return None, "Need project"

    @property
    def asset_name(self):
        """
        에셋 이름
        """
        return self._asset_name

    @asset_name.setter
    def asset_name(self, value):
        self._asset_name = value

    @property
    def asset_type(self):
        """
        에셋 타입
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, value):
        self._asset_type = value

    """
    프로젝트
    """

    def all_proj(self):
        """
        모든 프로젝트들
        """
        all_proj = gazu.project.all_projects()
        print("all project view")
        return all_proj

    def new_project(self, value):
        """
        새로운 프로젝트 생성,
        """
        new_proj = gazu.project.new_project(value)
        print("new proj")
        self._proj_name = new_proj

    def get_project(self, value):
        """
        get project by name
        """
        get_project = gazu.project.get_project_by_name(value)
        print("get proj")
        self._proj_name = get_project

    def rename_project(self,value):
        '''
        프로젝트 이름 변경
        '''
        print("전",self.proj_name) # 비포
        self.proj_name["name"] = value
        print("후",self.proj_name) # 에프터
        rename = gazu.project.update_project(self.proj_name)

    def close_project(self, value):
        """
        프로젝트 비활성화
        """
        close = gazu.project.close_project(value)
        print(value,"close proj")

    def remove_project(self, value):
        """
        프로젝트 삭제
        """
        gazu.project.remove_project(value)
        print(value, "remove proj")
    """
    에셋
    """
    def all_assets(self):
        """
        all assets type
        """
        all_assets = gazu.asset.all_asset_types()
        print("all assets view")
        return all_assets

    #     asset_types = gazu.asset.all_asset_types_for_project(a.new_project())

    def new_asset_type(self, value):
        """
        new 에셋 타입 추가     # asset_type = gazu.asset.new_asset_type("my new asset_type")
        """
        new_asset_type = gazu.asset.new_asset_type(value)
        print("new asset type")
        self._asset_type = new_asset_type

    def get_asset_type(self, value):
        """
        get asset
        """
        get_asset_type = gazu.asset.get_asset_type_by_name(value)
        print("get asset type")
        self._asset_type = get_asset_type



    def new_asset(self, asset, descrtpt):
        """
        에셋 추가     asset = gazu.asset.new_asset(prodict,asset_type,"cam1") #에셋 추가
        """
        proj_dict = self.proj_name
        asset_type_dict = self.asset_type
        asset_name = gazu.asset.new_asset(proj_dict, asset_type_dict, asset, descrtpt)
        print("new asset")
        self._asset_name = asset_name

    # def remove_asset_type(self, value):
    #
    #     gazu.asset.remove_asset_type(value)
    #     print("remove asset type")

    # def update_asset(self):

    # def remove_asset(self):


def main():
    a = HouChu()
    proj_name = "avata3"

    # pprint(a.all_proj())
    # a.new_project(proj_name)
    a.get_project(proj_name)
    # a.close_project(a.proj_name)
    '''
    proj name rename , remove
    '''
    rename_proj = "avata2"
    # a.rename_project(rename_proj)
    # a.remove_project(proj_name)

    '''
    에셋부분
    '''
    asset_type_name = "Cam_test"
    asset_type_descrtpt = ".abc"
    asset_name = "defult_Cam_03"

    # pprint(a.all_assets())
    # a.new_asset_type(asset_type_name)
    # a.get_asset_type(asset_type_name)
    # a.new_asset(asset_name, asset_type_descrtpt)

    # gazu.asset.remove_asset()


if __name__ == "__main__":
    main()

# project post
# projects = gazu.client.post("data/projects", {"name": "avata3"})
# print(projects)

# persons = gazu.person.all_persons()
# print(persons)

# tasks = gazu.user.all_tasks_to_do() # get user todo list  현재 로그인한 사용자의 할 일 목록
# print(1,tasks)
# persons = gazu.person.all_persons()
# sort_print(2,persons)

