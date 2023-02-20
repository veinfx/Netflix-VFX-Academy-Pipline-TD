'''
    숫자 야구 게임 

    num vs user  대결

    0 ~ 9 까지 숫자 3개 조합
    인덱스 0,1,2 사용

    스트라이크 , 볼, 아웃 

    변수 num,num_list,user,out,
'''

import random

from itertools import * # 겹치지않는 조합 


#   겹치지 않는 랜덤 3자리 수 num 만들기
class baseball:

    def __init__(self):
        self.num = str(random.randrange(100,999))
        num_list = list(range(self.num))

    





if __name__ == "__main__":
    main()