new_text= " Don`t remove Python ! \n Pleses!"

path= "/home/rapa/psw/py/230106/remember.txt"



# 방법 1


# f = open(path, "w")
# f.write(new_text)
# f.close()


# 방법 2 use with


# with open(path, "w") as f:
#         f.write(new_text)

with open(path, "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line)   #readline : 긴 문자열 , readlines : 한줄씩 리스트로 