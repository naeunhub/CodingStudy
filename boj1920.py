import sys

fir_length = sys.stdin.readline()
fir_list = set(sys.stdin.readline().split())

sec_length = sys.stdin.readline()
sec_list = sys.stdin.readline().split()

for sec in sec_list :
    if sec in fir_list :
        print(1)
    else :
        print(0)