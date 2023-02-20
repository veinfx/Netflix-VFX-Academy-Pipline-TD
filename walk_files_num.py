import os

path = '/home/rapa/project'

t = os.walk(path)
f_num = sum(
    map(len, list(k[2] for k in t))
)

print(f_num)