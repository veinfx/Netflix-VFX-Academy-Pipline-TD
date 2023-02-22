# 간 지 리스트 
gan_list = ["갑","을","병","정","무","기","경","신","임","계"]
ji_list = ["자","축","인","묘","진","사","오","미","신","유","술","해"]

# 년도 입력
def get_ganji(year_ganji):

    year_print = input("년도 입력 : ")


    #  1444년 갑자년 기준 

    yaer = int(year_print)

    ganji = (yaer - 1444) %60

    i = 0
    gan = 0 #10간
    ji = 0 # 12간

    for i in range(ganji):
        gan = gan + 1
        ji = ji + 1
        if gan == 10 :
            gan = 0
        if ji == 12:
            ji = 0
        year_ganji = gan_list[gan] +ji_list[ji]
        print(year_ganji)
        return 


# 예외처리하기 아규파서

import argparse,os,sys

def main():
    
    parser = argparse.ArgumentParser(
        description="This program is 년도 60간지 출력  프로그램입니다. 년도를 입력하세요 ! ", epilog = " 굿 ??")

    parser.add_argument("-y", type=int, help=" : year number 쓰세요 , ex) ~.py -y 2023")

    args = parser.parse_args()
    # print(args.y)
    get_ganji(year_ganji=args)
    return
    
    get_ganji(args.y)
    

    
if __name__ == "__main__":
    main()