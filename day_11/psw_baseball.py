'''
    숫자 야구 게임 

    rand range 9회

    num vs user  대결

    0 ~ 9 까지 숫자 
'''

import random

# 9가지의 랜덤 3자리수 리스트 

#숫자 하나씩 랜덤 randint 뽑아서 append (뒤에) str 으로 한 수 씩 추가 해서 3자리 range(3)

rand_num = str(random.randint(0,10))

















# for i in range(3):
    # rand_num = str(random.randint(0,10))
    # num = num_list[i+1]


# print(num_list) # 타입리스트

#     # 겹치지 않는 경우의수 조합


# # def check():
#     strike = 0   
#     ball = 0
#     out = 0
#     while True:
#         user=[]
#         i=0
#         for i in user[i]:
#             user[i] = input("f{i}번째 숫자를입력하시오:")
#             if user[i] == num_list[i]:
#                 print(user[i])
#             print(type(user))
            
#         for i in not user[i]:
#             out += i
#             continue

'''
for i in range(0,10):
    for j in range(1,10):
        for k in  range(2,10):
            # print(i,j,k, end=" ")
        
            print(random.choice(i))
'''

if __name__ == "__main__":
    main()