리눅스 쉘

ls -1

ls *.py

ls test?.py

pwd

touch 

echo "Hi”

cp /home/rapa/psw/test ~/psw/py/    >> copy

cp -f  >>> -f : 강제 덮어씌우기

mkdir

mv test_1 test

mkdir -p test/aaa/bbb/c

rm -rf   >> -r  ::  하위 지운다 

mv ~/psw/test/* ~/psw/test1 >> 묶고 싶은 하위폴더 모두 이동

df   >> PC 의 사용 용량 확인  

df -h   > 휴먼 스케일로 : 기가,바이트등등으로 

du > 현재폴더 사용확인 

du -h > -h: 같은 휴먼스케일로

cat

head > 헤드부분 ~ cat 

tail > 꼬리부분~ cat

[rapa@rapalab03 psw]$ which py3     >> 위치 확인

alias py3='/usr/bin/python3'
/usr/bin/python3

ls -1 > ~/ls.txt   >> ls -1 을 ls.txt 에 저장

[rapa@rapalab03 psw]$ echo "houdini" > ~/lss.txt
[rapa@rapalab03 psw]$ echo "houdini" >> ~/ls.txt    : >>  추가! 

ls | head : 파이프  : ls 를 head(10줄)만 보여줘 

mkdir imgs

mv imgs/ ~/

touch ~/imgs/filename.{0001..0010}.jpg

[rapa@rapalab03 ~]$ cd imgs/
[rapa@rapalab03 imgs]$ ls
filename.0001.jpg  filename.0004.jpg  filename.0007.jpg  filename.0010.jpg
filename.0002.jpg  filename.0005.jpg  filename.0008.jpg
filename.0003.jpg  filename.0006.jpg  filename.0009.jpg

[rapa@rapalab03 imgs]$ find ~/imgs/ -name "*.0010.jpg"
>> /home/rapa/imgs/filename.0010.jpg

[rapa@rapalab03 imgs]$ touch ~/imgs/filename.0011.jpg
[rapa@rapalab03 imgs]$ find ~/imgs/ -newer ~/imgs/filename.0009.jpg
/home/rapa/imgs/
/home/rapa/imgs/filename.0011.jpg      -nerwer : 그 뒤에 만든거 찾아줘

[rapa@rapalab03 imgs]$ find /home/rapa/imgs/ -name "

*.jpg" | grep 0006
/home/rapa/imgs/filename.0006.jpg
[rapa@rapalab03 imgs]$ find /home/rapa/imgs/ -name "*

.jpg" | grep 0006.jpg
/home/rapa/imgs/filename.0006.jpg

## 컴퓨터 체크

df -h  : 서버 용량확인

ifconfig  (윈도우는 ipconfig)

ping  : 핑 체크

top : 윈도우의 프로세스매니저 : 메모리 체크 

cp -a : archive : 아카이브

man cp  : cp 의 메뉴얼 

notify-send "hou”  : 알림 띄우는거 

crontab : 예약기능

[rapa@rapalab03 ~]$ crontab --help
crontab: 부적절한 옵션 -- '-'
crontab: usage error: unrecognized option
Usage:
crontab [options] file
crontab [options]
crontab -n [hostname]

Options:
-u <user>  define user
-e         edit user's crontab
-l         list user's crontab
-r         delete user's crontab
-i         prompt before deleting
-n <host>  set host in cluster to run users' crontabs
-c         get host in cluster to run users' crontabs
-s         selinux context
-V         print version and exit
-x <mask>  enable debugging

Default operation is replace, per 1003.2

crontab -e

30 10 5 1 * notify-send “houdini”   : 1월 5일 10시 30분 *주에 알람

30 10 * * 1-5 notify-send “houdini”  : 매주 월-금 10시 30분 알람

55 17 * * 1-5 notify-send “ 수업 종료시간 5분 전 “ : 매주 월~금 17시 55분에 알람

실무 : 정해진 시간에 서버 백업

- 쉘스크립트

[rapa@rapalab03 ~]$ touch [simple.sh](http://simple.sh/)

[rapa@rapalab03 ~]$ ./simple.sh
bash: ./simple.sh: 허가 거부
[rapa@rapalab03 ~]$ chmod 777 ./simple.sh
[rapa@rapalab03 ~]$ ./simple.sh
houdini

vi simple.sh

#!/bin/sh

hou="Houdini"

echo $hou

[rapa@rapalab03 ~]$ ./simple.sh
Houdini

[rapa@rapalab03 ~]$ vi [simple.sh](http://simple.sh/)

#!/bin/sh

hou="Houdini"

echo $hou

echo "What name?"

read MY_NAME

echo "Hi, $MY_NAME"

[rapa@rapalab03 ~]$ ./simple.sh
Houdini
What name?
입력>>sw
출력>>Hi, sw

[rapa@rapalab03 ~]$ vi [simple.sh](http://simple.sh/)

#!/bin/sh

#hou="Houdini"

#echo $hou

#echo "What name?"

#read MY_NAME

#echo "Hi, $MY_NAME"

#echo $1  아규먼트 실행 
#echo $2

>>>>>  [rapa@rapalab03 ~]$ ./simple.sh asdf fdsa

What name?
sw
Hi, sw
asdf
fdsa

if [ -f "$HOME/test.py" ]; then     : -f : 파일  -d : 디렉토리 
echo "홈 디렉터에 test.py가 존재합니다"

fi

>>>> 실무 : 특정파일 sh 깔려있으면 업데이트 , 없으면 설치할수 있게 td

- 파이썬

[rapa@rapalab03 230105]$ ls
test_0.py  test_1.py

test_0.py

```python
def print_text():
    print("hou")

def print_another():
    print("go away")    

def hi():
    print("HHI")

if __name__ == "__main__":
    print_text()
```

test_1.py

```python
import test_0

test_0.print_another()
```

test_2.py

```python
import test_0

test_0.hi()

--- test_3.py

## 함수가 길어지면

from tset_0 import print_another

print_another()

--- test_4.py

# 모두 불러올 때

from tset_0 import *

print_another()

```

```python
tree > API
```
