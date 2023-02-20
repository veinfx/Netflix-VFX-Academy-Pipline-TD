#2023 01 09 day 06

import os

path = "/home/rapa/psw/foo.jpg"

value = os.path.dirname(path) # /home/rapa/psw
value = os.path.exists(path) #실제 존재하는지 물어본다 True / False

os.path.expanduser("~") # >> '/home/rapa' 

os.path.getsize(path) #특정파일의 크기를 바이트로 알려준다 , 바이트 > 휴먼단위로 이해하기쉽게 나중에 확인할것

os.path.isfile(path) #실제 존재하는지 물어본다 True / False
os.path.isdir(path)

os.path.join('/home/rapa', 'asdf') 
'/home/rapa' + os.sep +'asdf'   #위랑 같게나오지만 path를 이용해서 쓰는게 낫다.

os.path.split(path)
# >> 스플릿 하면 
os.dirname(path), os.path.basename(path) #>>  "/home/rapa/psw/",  "foo.jpg"

os.rename(기존명, 바꿀명)
list = os.listdir(path)