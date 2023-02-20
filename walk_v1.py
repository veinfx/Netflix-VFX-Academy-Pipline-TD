import os

path = '/home/rapa/project'

t = os.walk(path)
for item in t:
    print(item)