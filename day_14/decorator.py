# def aaa_decorator(func):
# 	def wrapper():
# 		print("func start")
# 		func()
# 		print("func end")
# 	return wrapper

# @aaa_decorator
# def aaa():
# 	print("aaa")
# aaa()

# @aaa_decorator
# def bbb():
#     print("bbb")
# bbb()


# # @aaa_decorator
# # def aaa():
# # 	print("aaa")
# # aaa()
# # aaabb = aaa_decorator(aaa)
# # aaabb()

#arg 넣어보기

def print_deco(func):
    def wrapper(*args):
        print("func start") #2
        result = func(*args) #3
        print("func end") #4

        return result
    return wrapper

@print_deco
def sum(a,b):
    return a + b

# print(sum(1,2))

out = sum(1,2) #1 #5
print (out) #6


@print_deco
def mult(a,b):
    return a * b

print(mult(3,4))
