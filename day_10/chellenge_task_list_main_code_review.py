import json
import os
# to - do task list 만들기 add,edit,del
# my_list = []
# def main():    #task list add



data = []

path= "/home/veinfx/rapa/task_list.json"    # json 파일 저장 하는 곳
print("\n\n\njson 파일 경로 : ", path )

if os.path.exists(path) == False:    # json 파일 없을 시 만들어준다.
    with open(path,"w") as f:
        json.dump(data,f)



with open(path,"r") as f:
    data = json.load(f)
print("json 파일에 저장된  리스트 : " ,data)



def main():
    while True:
        
        print("\n")
        choice = input("\n\n        [   Task_List   ]    \n\n[ 추가 : a ] [ 리스트 : l ] [ 수정 : e ] [ 삭제 : d ] [ 초기화 : reset ] *[ 나가기 : q ] \n\n > 입력하시오 :  ")
        
        if choice == "a":
            add = input("할일을 추가하세요 : ")
            data.append(add)
            print("\nTask List : ",data)

        if choice == "e":                          
            for index,add in enumerate(data):
                print("index : ",index," > Task List : ", add)
            
            edit_num = int(input("수정할 인덱스를 선택하세요 : " ))
            
            # check
            if edit_num >= len(data):
                print("잘못된 입력값 처음부터 다시하시오 ")
                continue  
            if edit_num < 0:
                print("잘못된 입력값 처음부터 다시하시오 ")
                continue 
        
            edit = input("수정내용 : ")
            data[edit_num] = edit
            print("\n--> 수정 후 Task List : ", data)

                    
        if choice == "l":   #리스트 확인
            print("\n")
            for index,add in enumerate(data):
                
                print("index : ",index," > Task List : ", add)
            print("\n")         
        


        if choice == "d":       #삭제
            print("\n")
            for index,add in enumerate(data):
                print("index : ",index," > Task List : ", add)
            print("\n")
            
            del_num = int(input("삭제할 인덱스를 선택하세요 : "))

            # check
            if del_num >= len(data):
                print("잘못된 입력값 처음부터 다시하시오 ")
                continue   
            if del_num < 0:
                print("잘못된 입력값 처음부터 다시하시오 ")
                continue    
            del_list = data[del_num]

            print(" 삭제한 인덱스 : ", del_num)
            print(" 삭제한 할일 : ", del_list )


            del data[del_num]
            print("\n")
            print("삭제 후 Task_List : ", data)



        if choice == "reset":   #리셋
            print("진짜 초기화 할꺼 ? ")
            reset = input("삭제할꺼 ? : yes / no ")
            
            if reset == "yes":
                data.clear()

                print(data)
            if reset == "no":
                continue

        if choice == "q":
            print("최종 할일 리스트 : " ,data)
            total = len(data)
            print("총 할일 갯수 : ", total)

            break
        
        
        with open(path,"w") as f:
            json.dump(data,f, ensure_ascii=False)
                    # 아스키코드로 입력함. 인코딩 encoding

with open(path,"r") as f:
    data = json.load(f)
    print("최종 할일 리스트 : " ,data)
    total = len(data)
    print("총 할일 갯수 : ", total)

if __name__ == "__main__":
    main()

    