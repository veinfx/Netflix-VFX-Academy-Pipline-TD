import sys

class MyClass:
    def __init__(self) -> None:
        self._first_num = 0
        self._second_num = 0        
        pass

    @property
    def first_num(self) -> int: # 타입힌트 ->int
        return self._first_num

    @first_num.setter
    def first_num(self,value: int):     # int 받겠구나 타입힌트 강제성이없다 에러가안난다 . 스크립트 읽는사람들의 보여주기용
        # if not isinstance(int, value): #1번 밑에랑 같은뜻이다
            # exit(0)


        # try:

        
        # except Exception as e:
        #     raise Exception(e)


        if type(value) != int:    #2번
            sys.exit(0)
        #     raise ValueError("not int")
        #     raise Exception("error")

        # assert type(value) == int   #3번 assert 로 raise 에러발생

        self._first_num = value

    @property
    def second_num(self):
        return self._first_num

    @second_num.setter
    def second_num(self,value):
        self._second_num = value

    def add_num(self):
        return self.first_num + self.second_num
    def minus_num(self):
        return self.first_num - self.second_num


    def main():
        mc = MyClass()
        mc.first_num = 1
        print(mc.first_num)

        a = "asdf" 
        a.title()   # a만 대문자로 
        a.lower()
        a.upper()

    if __name__ == "__main__":
        main()