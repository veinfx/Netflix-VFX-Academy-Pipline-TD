import argparse

parser = argparse.ArgumentParser(description="This program is good ! ",epilog="good?") 

#description="This program is good ! " 설명

parser.add_argument("-p", "--project", help="Project name")
parser.add_argument("-q", "--seq", help="seq name")
parser.add_argument("-s", "--shot", help="shot name")

args = parser.parse_args()

#


print(args.project, args.seq, args.shot)
