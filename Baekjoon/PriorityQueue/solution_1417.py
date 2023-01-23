import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    slist = list(map(str, sys.stdin.readline().split()))
    list = []

    for _ in range(n):
        cmd = slist[0]
        m = int(slist[1])

        if cmd == 'push':
            list.append(int(m))
        elif cmd == 'pop':
            if len(list) == 0:
                print(-1)
            else:
                print(list.pop(-1))
                print(list.remove(-1))
        elif cmd == 'size':
            print(len(list))
        elif cmd == 'empty':
            if len(list) == 0:
                print(0)
            else:
                print(1)
        else:
            if len(list) == 0:
                print(-1)
            else:
                print(list.pop(-1))