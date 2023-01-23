import sys

x = int(input())
for i in range(x):
    nums = list(map(int, sys.stdin.readline().split()))
    nums.sort()
    print(nums[-3])