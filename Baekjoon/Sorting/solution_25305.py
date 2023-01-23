import sys

n, k = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
l.sort()
print(l[-k])