import argparse

# to - do task list 만들기 add,edit,del
# my_list = []

# def main():    #task list add
    
    
task_list=[]

while True:
    print("\n")
    choice = input(" [  Task_List 만들기    ] \n add : a , edit : e , read : r , delet : d, quit : q \n\n")
    
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
 

    if choice == "r":
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
        
        del task_list[del_num]
        print("\n")
        print("삭제 후 Task_List : ", task_list)

    if choice == "q":
        break
    
        



# def edit():
#     return



# if __name__ == "__main__":
#     main()

    