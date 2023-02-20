'''
터미널에서 task list 만들기 ~

설정된 기능들       실행 keys

        추가 (add) : a
        리스트 (list 보기 ) : l 
        수정 (edit) : e
        삭제 (del) : d
        초기화 (reset) : reset      reset 시  한번더 재확인 함
        나가기와 동시에 저장 (quit) : q


'''




import os, json

data = []

# json 파일 경로
path= "/home/rapa/psw/task_list.json"
print("\n\n\njson 파일 경로 : ", path )


 # json 파일이 없을경우 / 경로 내 디렉토리없으면 오류 > 디렉토리없을경우도 수정예정
if os.path.exists(path) == False:   
    with open(path,"w") as f:
        json.dump(data,f)


#json read
with open(path,"r") as f:
    data = json.load(f)
print("json 파일에 저장된  리스트 : " ,data)



def main():
    while True:
        
        print("\n")
        choice = input("\n\n        [   Task_List   ]    \n\n[ 추가 : a ] [ 리스트 : l ] [ 수정 : e ] [ 삭제 : d ] [ 초기화 : reset ] *[ 나가기 & 저장 : q ] \n\n > 입력하시오 :  ")
        
#추가
        if choice == "a":
            add = input("할일을 추가하세요 : ")
            data.append(add)
            print("\nTask List : ",data)
#리스트                   
        if choice == "l":
            print("\n")
            for index,add in enumerate(data):
                print("index : ",index," > Task List : ", add)
            print("\n")         
#수정
        if choice == "e":                          
            for index,add in enumerate(data):
                print("index : ",index," > Task List : ", add)
            
            try:
                edit_num = int(input("수정할 인덱스를 선택하세요 : " ))
                # check
                if edit_num >= len(data):
                    print("잘못된 입력값 처음부터 다시 하시오 ")
                    continue  
                if edit_num < 0:
                    print("잘못된 입력값 처음부터 다시 하시오 ")
                    continue 
            except ValueError:
                print("어허 이상한거 입력하지마세요. 인덱스를 잘보고 택1 ")
                continue
            
            edit = input("수정내용 : ")
            data[edit_num] = edit
            print("\n--> 수정 후 Task List : ", data)
#삭제
        if choice == "d":
            print("\n")
            for index,add in enumerate(data):
                print("index : ",index," > Task List : ", add)
            print("\n")
            
            try:    
                del_num = int(input("삭제할 인덱스를 선택하세요 : "))
           
                # check
                if del_num >= len(data):
                    print("잘못된 입력값 처음부터 다시 하시오 ")
                    continue   
                if del_num < 0:
                    print("잘못된 입력값 처음부터 다시 하시오 ")
                    continue
            except ValueError:
                print("당신은 이상한사람?! .. 인덱스를 선택하시오!! ")
                continue

            del_list = data[del_num]

            print(" 삭제한 인덱스 : ", del_num)
            print(" 삭제한 할일 : ", del_list )

            del data[del_num]
            print("\n")
            print("삭제 후 Task_List : ", data)
#리셋
        if choice == "reset": 
            print("진짜 초기화 할꺼 ? ")
            reset = input("삭제할꺼 ? ( yes / no ) 택1\n:")
            
            if reset == "yes":
                data.clear()

                print(data)
            if reset == "no":
                continue
#나가기 와 저장 
        if choice == "q":
            print("최종 할일 리스트 : " ,data)
            total = len(data)
            print("총 할일 갯수 : ", total)
            break
        
        
        with open(path,"w") as f:
            json.dump(data,f, ensure_ascii=False)
                    # 아스키코드로 입력함. 인코딩 encoding

#최종 리스트와 할일 갯수 출력 
with open(path,"r") as f:
    data = json.load(f)
    print("최종 할일 리스트 : " ,data)
    total = len(data)
    print("총 할일 갯수 : ", total)

if __name__ == "__main__":
    main()