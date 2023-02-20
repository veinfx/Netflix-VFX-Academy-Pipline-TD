
import os, csv

path = os.path.expanduser('~/cas_tset_v01.csv')

mydict = {}
with open(path, mode='r') as file:
    reader = csv.reader(file)
    attrs = []
    result = []
    for row in reader:
        if len(attrs) < 1:
            attrs = row
            continue
        temp_row_dict = dict()
        for key, value in zip(attrs, row):
            temp_row_dict[key] = value
        result.append(temp_row_dict)


for row in result:
    print(row)