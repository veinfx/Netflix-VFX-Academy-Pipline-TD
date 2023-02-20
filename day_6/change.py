# foo > far

import os
import re

# path = '/home/rapa/project/'

# dirlist = os.listdir(path)

# print(dirlist)



# def DirCheck(path):
#     file_list = os.listdir(path)
#     for name in file_list:
#         new_path = os.path.join(path.name)
#         #print("path" + new_path)
#         if os.path.isdir(new_path):
#             print(name + ":폴더")
#             Rename(name,new_path, path)
#         elif os.path.isdir(new_path):
#             print("폴더 시작")
#             DirCheck(new_path)
#             print("폴더 확인")
#         else:
#             print(name + ": 아무것도아님")

# def Rename(name, before_path, after_path):
#     old_name = "foo"
#     new_name = str(name)
#     new_name = new_name.replace(old_name,"")
#     os.rename(before_path, after_path + "/" + new_name)
#     print(new_name)

# DirCheck(path)



# name = os.listdir(path)

# i = 1

# for name in name:
#     src = os.path.join(path,name)
#     dst = format(i, '03')
#     dst = os.path.join(path,dst)
#     os.rename(src,dst)

#     i+=1



# main_folder = r'/home/rapa/project/' # 검색 폴더 위치

# for item in os.listdir(main_folder): # 해당 폴더 내 모든 파일 및 폴더 추출

#     sub_folder = os.path.join(main_folder, item)

#     if os.path.isdir(sub_folder): # 폴더 여부 확인
        
#         print(sub_folder)


#여러 폴더가 있는 경로
folderpath = r'/home/rapa/project/'

#폴더명 받아오기
folderlist = os.listdir(folderpath)

#폴더명 리스트 출력해보기
print(folderlist)



i=0 #파일명 변경하기 위한 넘버링 변수

#폴더리스트를 for문을 통해 반복
for fname1 in folderlist:
    #해당 test 폴더(1,2,3,4) 위치 설정
    current_folder = folderpath + "/" + fname1
    #각 test폴더(1,2,3,4) 안의 파일명 받아오기
    filelist = os.listdir(current_folder)

    print("현재 폴더명 : ", fname1)
    #각 폴더명의 파일리스트를 다시 for문을 통해 반복
    for fname2 in filelist:
        #os.rename(a, b) : a를 b로 이름 변경. b는 저장될 위치도 지정하는 것이므로 같은 폴더에하려면 폴더명 지정
        print(fname2+"를 이름바꾸기"+str(i)+".jpg로 파일명을 변경합니다.")
        os.rename(current_folder+"/"+fname2, "test"+str(i)+".jpg")
        i = i+1




 