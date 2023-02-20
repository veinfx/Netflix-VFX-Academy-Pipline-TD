# 간 지 리스트 
gan_list = ["갑","을","병","정","무","기","경","신","임","계"]
ji_list = ["자","축","인","묘","진","사","오","미","신","유","술","해"]

# 년도 입력

str_input = input("년도 입력 : ")

#  1444년 갑자년 기준 

birth_yaer = int(str_input)

ganji = (birth_yaer - 1444) %60

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
print(gan_list[gan],ji_list[ji])



