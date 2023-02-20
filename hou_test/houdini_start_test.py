import os

class Launch:
    def __init__(self):
        self.home_path = os.path.expanduser('/')
        self.home_user = input("pwd path : '/' + cd : ")
        self.houdini_dir = 'hfs' + input("hfs + 버전명 : ")
        self.path = os.path.join(self.home_path, self.home_user, self.houdini_dir) + '/bin/'

    # def ver_num_check(self):
    #     self.split_houdini_path = self.houdini_dir.split(' ')        
    #     while self.split_houdini_path[1].isalpha():
    #         print("숫자를 입력하세요\nex. 19.0.657")
    #         self.home_user = input("version: ")
    #         if self.split_houdini_path[1].isdigit():
    #             break 
    #         return
    
    def path_exists(self):        
        while not os.path.exists(self.path):
            print("없는 경로입니다.")
            self.rename_user = input("users name: ")
            self.start = os.path.join(self.home_path, self.rename_user, self.houdini_dir) + '/bin/houdini.exe'
       
            # if os.path.exists(self.path):
            #     break
            return

def main():
    path = Launch()
    # path.ver_num_check()
    path.path_exists()
    os.system('path')

if __name__ == "__main__":
    main()