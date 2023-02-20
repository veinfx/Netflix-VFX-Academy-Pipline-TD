import random

list = []

ran_num = str(random.randint(0,999))

print(ran_num)

print(type(ran_num))
for i in range(3):
    print(ran_num[i])
    i+=1


# for i in range(1):
#     while ran_num in list:
#         ran_num = random.randint(0,999)
#     list.append(ran_num)

# print(list)