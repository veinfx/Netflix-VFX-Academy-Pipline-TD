import subprocess

cmd = "zenity --password --username"
cmd_list = ["zenity", "--password", "--username"]
p = subprocess.Popen(cmd_list,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,universal_newlines=True)
 #스탠다드 인자를 받으려면 Popne

while p.poll() == None:
# poll 실행이 끝날때까지 기다리는거
    out = p.stdout.readline()
    print(out)