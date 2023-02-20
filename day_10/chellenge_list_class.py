import json

# to - do task list 만들기 add,edit,del
# my_list = []

# def main():    #task list add
    
  
task_list=[]

path = "/home/rapa/json_test.json"

print("\njson 파일 경로 : ", path )



while True:
    with open(path,"r") as f:
        data = json.load(f)
    # data_n = f.readlines(data)
    # for datas in data_n:   # >> json은 딕셔너리라서 lines 안된다 !

    print("json 할일 리스트 : " ,data)



    print("\n")
    choice = input("        [  Task_List   ]    \n 추가 : a , 수정 : e , 리스트 : l , 삭제 : d, 나가기 : q \n\n")
    
    if choice == "a":
        add = input("할일을 추가하세요 : ")
        task_list.append(add)
        print("\nTask List : ",task_list)

    if choice == "e":
        for index,add in enumerate(task_list):
        
            print("index : ",index," > Task List : ", add)   
            # print(task_list)
            
            

        edit_num = int(input("수정할 인덱스를 선택하세요 : " ))
        ## -- 여까지 됨

        edit = input("수정내용 : ")
        task_list[edit_num] = edit

        # task_list[edit_num] = edit
        
        print(task_list)


                    
            # for edit_num in index:
            #     edit = task_list[edit_num]
            #     print(task_list)
                
            # edit_num = int(input("수정할 인덱스를 선택하세요 : " , task_list))
            
            # edit = task_list[edit_num]
            # edit = str(input("수정 사항 : "))

            # print(task_list)       
 

    if choice == "l":
        print("\n")
        for index,add in enumerate(task_list):
            
            print("index : ",index," > Task List : ", add)
        print("\n")
    


    if choice == "d":
        print("\n")
        for index,add in enumerate(task_list):
            print("index : ",index," > Task List : ", add)
        print("\n")
        
        del_num = int(input("삭제할 인덱스를 선택하세요 : "))
        a = task_list[del_num]

        print(" 삭제한 인덱스 : ", del_num)
        print(" 삭제한 할일 : ",a )


        del task_list[del_num]
        print("\n")
        print("삭제 후 Task_List : ", task_list)
        # print(del_num)
        # print(a)
        

    if choice == "q":
        break
    
    
    with open(path,"w") as f:
        json.dump(task_list,f)


with open(path,"r") as f:
    data = json.load(f)
		# data_n = f.readlines(data)
    # for datas in data_n:   # >> json은 딕셔너리라서 lines 안된다 !
    
    print("json 할일 리스트 : " ,data)



# def edit():
#     return



# if __name__ == "__main__":
#     main()

    