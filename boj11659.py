import sys

input = sys.stdin.readline
N, M = map(int, input().split(" "))
numbers = list(map(int, input().split(" ")))

sum_= [0]
total = 0
for idx in range(len(numbers)) :
    total+=numbers[idx]
    sum_.append(total)

for idx_ in range(M) :
    i, j = map(int, input().split(" "))
    print(sum_[j]-sum_[i-1])