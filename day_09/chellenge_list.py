import argparse

# to - do task list 만들기 add,edit,del
# my_list = []


# def main():    #task list add
    
    
task_list=[]

while True:
    choice = input("add : a , edit : e , read : r , delet : d, quit : q\n")
    
    if choice == "a":
        add = input("할일을 추가하세요 : ")
        task_list.append(add)
        print(task_list)

    if choice == "e":
        edit_num = input("수정할 인덱스를 선택하세요 : ")
        edit = task_list[edit_num]
        edit = str(input("수정 사항 : "))
        print(task_list)       
 

    if choice == "r":

        for index,add in enumerate(task_list):
            
            print(index, add)
    
    if choice == "d":
        del_num = input("삭제할 인덱스를 선택하세요 : ")
        
        del task_list[del_num]

        print(task_list)

    if choice == "q":
        break
    
        



# def edit():
#     return



# if __name__ == "__main__":
#     main()

    