import sys

def pre_order(v):
    if v:
        print(v, end='')
        pre_order(ch1[check[v]])
        pre_order(ch2[check[v]])

def in_order(v):
    if v:
        in_order(ch1[check[v]])
        print(v, end='')
        in_order(ch2[check[v]])

def post_order(v):
    if v:
        post_order(ch1[check[v]])
        post_order(ch2[check[v]])
        print(v, end='')

n = int(sys.stdin.readline())
ch1 = [''] * (n + 1)
ch2 = [''] * (n + 1)
check = {}

for i in range(1, n + 1):
    x, y, z = sys.stdin.readline().split()
    check[x] = i
    if y != '.':
        ch1[i] = y
    if z != '.':
        ch2[i] = z

pre_order('A')
print()
in_order('A')
print()
post_order('A')