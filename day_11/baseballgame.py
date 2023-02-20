'''
    숫자 야구 게임 

    rand range 9회

    num vs user  대결

    0 ~ 9 까지 숫자 
'''

import random

from itertools import *

# 9가지의 랜덤 3자리수 리스트 

def rand_num():
    num_list = []
    num = str(random.samplelen(10),3)
    
    num_list = list(num)

print(rand_num())
    # num = permutations(num_list,9)
    
    # print(type(num))
    # print(num)




    # for i in range(len(num)):
    #     print(num[i])
        
    # num_list = range(len(num))
    # num_9 = permutations(num,9)
    # print(num_9)


# print(num)
# print(type(num))


# user = input("3자리 숫자입력 : ", user_num)
# num = range(10)
# num()
# print(num)

# while True:
#     num
#     for num in range(()):
#         print(num)
# for i in range(0,10):
#     i +=1
#     if i > 10: continue

# roop = 0
# for i,j,k in num:
#     roop += 1
#     if roop < 10:

    # def num(self,i,j,k):

    #     self = random.randrange(0,10)
        
# print(type(i))
# print(i,j,k)
# num = i,j,k

# print (num)
# print(type(num))
# print(num[1])

# # user_num 

# user_num = input("숫자입력:")

# print(user_num[0])

# while True:
#     roop = 0
#     stk = 0
#     ball = 0
#     if roop < 10:
        




#9회 돌린다
# roop = 0
# while roop < 10:
#     roop+=1
#     if user_num in num:
        








    
'''
for i in range(0,10):
    for j in range(1,10):
        for k in  range(2,10):
            # print(i,j,k, end=" ")
        
            print(random.choice(i))
'''
# i = random.randrange(0,10)

# print(random.choice(i))
# print(i)

# for roop in num:
#     roop += roop
#     print(i)


# while True:
#     stk = 0
#     ball = 0
#     user = int(input("숫자입력:"))
    
#     print(user)
    

#     for i in user:

#         if user == num:
#             print("스트라이크")
#         elif user != num:
#             print("볼")
#         else :
#             print("None")
#     if i > 10:
#         print("9회 끝")
#         break

# if __name__ == "__main__":
#     main()