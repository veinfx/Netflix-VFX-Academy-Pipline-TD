new_text= " Don`t remove Python ! \n Pleses!"

path= "/home/rapa/psw/py/230106/remember.txt"



# 방법 1


# f = open(path, "w")
# f.write(new_text)
# f.close()


# 방법 2 use with


# with open(path, "w") as f:
#         f.write(new_text)

# with open(path, "r") as f:
#     lines = f.readlines()
#     for line in lines:
#         print(line)   #readline : 긴 문자열 , readlines : 한줄씩 리스트로 


#.json 사용

import json
sample_dict = {
    "foo" : "aa",
    "bar" : 1,
    "hou" : ["1","b",3],
    "fsz" : {
        "a" :5
    }
}

#쓰기

path = "/home/rapa/psw/py/json_text.json"
with open(path,"w") as json_file:
    json.dump(sample_dict, json_file, indent = 2 ) # indent : 띄어씌기옵션

#읽기

data = {} #타임선언
with open(path,"r") as f:
    data = json.load(f)

    # data_n = f.readlines(data)
    # for datas in data_n:   # >> json은 딕셔너리라서 lines 안된다 ! 
    
    print(data)
