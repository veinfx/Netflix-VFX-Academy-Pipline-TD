'''
터미널에서 task list 만들기 ~

설정된 기능들    실행 keys

        추가 (add)          : a
        리스트 (list 보기 ) : l 
        수정 (edit)         : e
        삭제 (del)           : d
        초기화 (reset)      : reset      
        나가기와 동시에 저장 (quit) : q
'''

import os, json

# json 파일 경로
path= "/home/rapa/psw/task_list.json"         # rapa 교육장

# path= "/home/veinfx/rapa/task_list.json"        # veinfx sw home 우분투
print("\n\n\njson 파일 경로 : ", path )


class todo():

    def __init__(self):
        self.choice = ''
        self.data = []

         # json 파일이 없을경우 파일만들어줌!                    >  경로 내 디렉토리없으면 오류 > 디렉토리없을경우도 넣어야하나..허허
        if os.path.exists(path) == False:   
            self.save()
        
        self.load()
        pass
                
   
#추가
    def add(self):

        add = input("할일을 추가하세요 : ")
        self.data.append(add)
        print("\nTask List : ",self.data)

#리스트
    def list(self,data):                   
        print("\n")
        for index,add in enumerate(data):
            print("index : ",index," > Task List : ", add)
        print("\n")         
                
#수정   
    def edit(self,edit_num):                      
        for index,add in enumerate(self.data):
            print("index : ",index," > Task List : ", add)
        
        try:
            edit_num = int(input("수정할 인덱스를 선택하세요 : " ))
            # check
            if edit_num >= len(self.data):
                print("잘못된 입력값 처음부터 다시 하시오 ")
                return  
            if edit_num < 0:
                print("잘못된 입력값 처음부터 다시 하시오 ")
                return 
        except ValueError:
            print("어허 이상한거 입력하지마세요. 인덱스를 잘보고 택1 ")
            return
        
        edit = input("수정내용 : ")
        self.data[edit_num] = edit
        print("\n--> 수정 후 Task List : ", self.data)

#삭제
    def delete(self,del_num):
        print("\n")
        for index,add in enumerate(self.data):
            print("index : ",index," > Task List : ", add)
        print("\n")
        
        try:    
            del_num = int(input("삭제할 인덱스를 선택하세요 : "))
    
            # check
            if del_num >= len(self.data):
                print("잘못된 입력값 처음부터 다시 하시오 ")
                return   
            elif del_num < 0:
                print("잘못된 입력값 처음부터 다시 하시오 ")
                return
        except ValueError:
            print("당신은 이상한사람?! .. 인덱스를 선택하시오!! ")
            return

        del_list = self.data[del_num]

        print(" 삭제한 인덱스 : ", del_num)
        print(" 삭제한 할일 : ", del_list )

        del self.data[del_num]
        print("\n")
        print("삭제 후 Task_List : ", self.data)

#리셋
    def reset(self):

        print("진짜 초기화 할꺼 ? ")
        reset = input("삭제할꺼 ? ( yes / no ) 택1\n:")
        
        if reset == "yes":
            self.data.clear()
            
            # print(data)
        elif reset == "no":
            pass
        else:
            print("잘못 된 입력 값 ! 다시 처음으로 ")
            
        self.list_total()

# 리스트 and 갯수 출력
    def list_total(self):
        print("최종 할일 리스트 : " ,self.data)
        total = len(self.data)
        print("총 할일 갯수 : ", total)

#data 저장
    def save(self):  
        with open(path,"w") as f:
            json.dump(self.data,f, ensure_ascii=False)        # 아스키코드로 입력함. 인코딩 encoding
        self.list_total()

#리스트 read  
    def load(self):
        with open(path,"r") as f:
            self.data = json.load(f)
        self.list_total()

        print("aaa")

            # print("할일 리스트 : " ,data)
            # total = len(data)
            # print("총 할일 갯수 : ", total)


def main():
    
    task = todo()

    while True:

        print("\n")
        choice = input("\n\n        [   Task_List   ]    \n\n[ 추가 : a ] [ 리스트 : l ] [ 수정 : e ] [ 삭제 : d ] [ 초기화 : reset ] *[ 나가기 & 저장 : q ] \n\n > 입력하시오 :  ")

        if choice == "a":
            task.add()

        elif choice == "l":
            task.list(task.data)

        elif choice == "e":
            task.edit(choice)

        elif choice == "d":
            task.delete(task.data)

        elif choice == "reset":
            task.reset()

        elif choice == "q":
            task.save()
            return

        else:
            task.save()
            print(" 중간 저장 되었음 다시실행하시오")
            return


if __name__ == "__main__":
    main()