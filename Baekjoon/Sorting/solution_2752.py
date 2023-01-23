import sys

list = list(map(int, sys.stdin.readline().split()))
list.sort()
for i in list:
    print(i, end=" ")
