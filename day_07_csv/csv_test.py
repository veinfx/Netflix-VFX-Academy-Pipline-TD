import os
import csv

csv_path = os.path.expanduser('~/csv_data.csv')
#save

#쓰기
with open(csv_path, 'w') as f:
    writer = csv.writer(f)   # writer 저장도와주는놈
    writer.writerow(["number", "name", "info"])
    writer.writerow(["1", "adidas", "small"])
    writer.writerow(["2", "nike", "tall"])

#읽기

with open(csv_path, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        