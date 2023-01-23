import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    lst = []
    for i in range(n):
        lst.append(sys.stdin.readline().strip())
    set_list = set(lst)
    lst = list(set_list)
    lst.sort()
    lst.sort(key = len)

    for i in lst:
        print(i)
