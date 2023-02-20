import os
import re
import csv

def get_regx_name(file_path):
    file_info_name = re.sub(r'(.+/\w+_\w+_\w+_v\d{3}\.)\d{4}\.jpg$', r'\1####.jpg', file_path, flags=re.IGNORECASE)
                            #r 레귤러 명시용                         # jpg 대문자 무시: flags=re.IGNORECASE
                                                                    # '\1####\2' \1 : 첫번째 그룹, \2 두번째그룹
    print(file_path, file_info_name)
    return file_info_name

def search_files(path):
    data = {}
    if not os.path.exists(path):
        return data

    for roots, _, files in os.walk(path):
        for file_name in files:
            #file_name = file_name.lower() ## 치환비추 csv 파일 모두 소문자로 바뀐다
            if not file_name.lower().endswith('.jpg'): # lower() 소문자로 바꿈
                continue
            file_path = os.path.join(roots, file_name)
            file_info_name = get_regx_name(file_path)
            if file_info_name not in data:
                data[file_info_name] = []
            data[file_info_name].append(file_path)

    return data

def get_info(file_path):
    info = {
        "project" : None,
        "seq" : None,
        "shot" : None,
        "version" : None
        
    }
    r = re.search('.+/project/(\w+)/shot/(\w+)/(\d{4})/\w+/(v\d{3})', file_path)
    if r:
        info['project'] = r.group(1)
        info['seq'] = r.group(2)
        info['shot'] = r.group(3)
        info['version'] = r.group(4)
    return info

def get_frame_info(file_lst):
    """
    파일 리스트를 받아서 first frame과 last frame을 찾아 반환한다.
    """
    sorted_list = sorted(file_lst)
    first_file = sorted_list[0]
    last_file = sorted_list[-1]
    #/home/rapa/project/avata/shot/boo/0010/plate/v001/boo_0010_plate_v001.0005.jpg
    m = re.compile('.+/\w+_\w+_\w+_v\d{3}\.)\.(\d{4})\.jpg$')
    first_re = m.search(first_file)

    if first_re:
        first = first_re.group(1)
        
    last_re = m.search(last_file)
    if last_re:
            last = last_re.group(1)
    return first,last

def save_csv(data):
    csv_path = os.path.expanduser('~/project.csv')

    with open(csv_path, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['project', 'seq', 'shot', 'version', 'frame', 'path'])

        for file_dir_path in data:
            info = get_info(file_dir_path)
            frame_info = get_frame_info(data[file_dir_path])
            writer.writerow([info['project'], info['seq'], info['shot'], info['version'], len(data[file_dir_path]), file_dir_path])

def main():
    path = os.path.expanduser('~/project')
    data = search_files(path)
    save_csv(data)

if __name__ == "__main__":
    main()
