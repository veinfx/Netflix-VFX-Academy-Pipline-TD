import os
import re
import sys

def change_name(path, pattern, repl):
    '''
    path의 tail 부분에서 pattern을 찾아 repl(replacement)로 교체
    '''
    dirname, old_filename = os.path.split(path)
    # 이름 전체가 일치하는 경우에만 변경되도록 전방, 후방 탐색 이용
    
    exact = '(?<![a-zA-Z0-9])' + pattern + '(?![a-zA-Z0-9])' # : 전체 변경 , 정규표현식전방탐색

    # exact = "^" + pattern + "$"    # ^ : 시작을 의미 , $ :끝을 의미 : 절대경로 디렉토리만 변경

    new_filename = re.sub(exact, repl, old_filename)
    os.rename(os.path.join(dirname, old_filename), os.path.join(dirname, new_filename))

def traversal_path(path, pattern, repl):
    '''
    path를 순회하면서 파일 혹은 디렉토리의 이름을 변경하는 함수
    '''
    if os.path.isdir(path):
        children = os.listdir(path)
        for child in children:
            child_path = os.path.join(path, child)
            traversal_path(child_path, pattern, repl)
    
    change_name(path, pattern, repl)


if __name__ == '__main__':
    argv = sys.argv[1:]
    if len(argv) != 2:
        print('error : pattern과 repl 값을 지정해주세요.')
    else:
        pattern, repl = argv
        project_path = '/home/rapa/project' 
        traversal_path(project_path, pattern, repl)
        # traversal_path(path, 'foo', 'far')
        # os.system('tree ' + project_path)
        print('\t 변경 완료 : ' + pattern + ' --> ' + repl +'\n')
    