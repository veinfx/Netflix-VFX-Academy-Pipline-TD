import json

# to - do task list 만들기 add,edit,del
# my_list = []

# def main():    #task list add




path = "/home/rapa/json_test.json"

print("\njson 파일 경로 : ", path )

with open(path,"r") as f:
    data = json.load(f)
# data_n = f.readlines(data)
# for datas in data_n:   # >> json은 딕셔너리라서 lines 안된다 !

print("json 파일에 저장된  리스트 : " ,data)

def main():
    while True:
        
        print("\n")
        choice = input("        [   Task_List   ]    \n\n*추가 : a    *수정 : e    *리스트 : l    *삭제 : d  *초기화 : reset    *나가기 : q \n\n : ")
        
        if choice == "a":
            add = input("할일을 추가하세요 : ")
            data.append(add)
            print("\nTask List : ",data)

        if choice == "e":
            for index,add in enumerate(data):
                print("index : ",index," > Task List : ", add)     
                edit_num = int(input("수정할 인덱스를 선택하세요 : " ))
                if edit_num == index:
                    edit = input("수정내용 : ")
                data    [edit_num] = edit
                
                else edit_num != index:  
                print("잘못된 입력값 처음부터 다시하시오 ")
                break
                print("\n   -->    수정 된 Task List : ", data)
                # for edit_num in index:
                #     edit = task_list[edit_num]
                #     print(task_list)
                    
                # edit_num = int(input("수정할 인덱스를 선택하세요 : " , task_list))
                
                # edit = task_list[edit_num]
                # edit = str(input("수정 사항 : "))

                # print(task_list)       
    

        if choice == "l":
            print("\n")
            for index,add in enumerate(data):
                
                print("index : ",index," > Task List : ", add)
            print("\n")
        


        if choice == "d":
            print("\n")
            for index,add in enumerate(data):
                print("index : ",index," > Task List : ", add)
            print("\n")
            
            del_num = int(input("삭제할 인덱스를 선택하세요 : "))
            a = data[del_num]

            print(" 삭제한 인덱스 : ", del_num)
            print(" 삭제한 할일 : ",a )


            del data[del_num]
            print("\n")
            print("삭제 후 Task_List : ", data)
            # print(del_num)
            # print(a)

        if choice == "reset":
            print("진짜 초기화 할꺼 ? ")
            reset = input("삭제할꺼 ? : yes / no ")
            
            if reset == "yes":
                data.clear()

                print(data)
            if reset == "no":
                continue

        if choice == "q":
            break
        
        
        with open(path,"w") as f:
            json.dump(data,f, ensure_ascii=False)
                    # 아스키코드로 입력함. 인코딩 encoding

with open(path,"r") as f:
    data = json.load(f)
        # data_n = f.readlines(data)
    # for datas in data_n:   # >> json은 딕셔너리라서 lines 안된다 !

    print("최종 할일 리스트 : " ,data)
    total = len(data)
    print("총 할일 갯수 : ", total)



# def edit():
#     return



if __name__ == "__main__":
    main()

    