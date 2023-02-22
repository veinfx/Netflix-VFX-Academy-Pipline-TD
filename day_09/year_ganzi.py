# 2023은 계묘년 입니다.

# #### 년도를 입력받아 60간지를 반환하는
# 프로그램을 만들어보세요

# 10간지 : 갑을병정무기경신임계
# 16간지 : 자축인묘진사오미신유 술해

import os
import csv

csv_path = os.path.expanduser('~/ganzi_program.csv')

# def ganzi_list():
#     # csv_path = os.path.expanduser('~/ganzi_program.csv')

with open(csv_path, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["갑","을","병","정","무","기","경","신","임","계"])
    writer.writerow(["자","축","인","묘","진","사","오","미","신","유","술","해"])

with open(csv_path, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

a = ["a","b","c"]
b = ["d","e","f","g"]

for i in a:
    print(i)

dict = dict(zip(a,b))
print(dict)



# import argparse
# parser = argparse.ArgumentParser





# if __name__ == "__main__":
    