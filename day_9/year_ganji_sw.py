# 간 지 리스트 
gan_list = ["갑","을","병","정","무","기","경","신","임","계"]
ji_list = ["자","축","인","묘","진","사","오","미","신","유","술","해"]

# 년도 입력

str_input = input("년도 입력 : ")

#  1444년 갑자년 기준 

yaer = int(str_input)

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
# # 예외처리하기 아규파서

# import argparse

# def main():
#     parser = argparse.ArgumentParser(description="This program is 60간지 출력  프로그램입니다. 년도를 입력하세요 ! ", epilog = " 굿 ??")

#     parser.add_argment("-y", "--year", help = "year name")

#     args = parser.parse_args()

#     print(args.year)



# if __name__ == "__main__":
#     main()

