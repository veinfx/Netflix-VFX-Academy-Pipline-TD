
import lucidity

template = lucidity.Template(
    'model','/home/rapa/project/{project}/shot/{seq}/{shot}/'
            '{dept}/{ver}/{seq}_{shot}_{dept}_{ver}.{padding}.{ext}'
)

print(template.keys())

path = '/home/rapa/project/avata/shot/boo/' \
       '0010/plate/v001/boo_0010_plate_v001.0001.jpg'

data = template.parse(path)
print(data['seq'])