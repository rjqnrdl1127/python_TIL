import sys

def sort(arr):
    count = 0
    isFind = False
    for i in range(len(arr) - 1, 0, -1):
        target = i
        max = arr[i]
        for j in range(i - 1, -1, -1):
            if max < arr[j]:
                max = arr[j]
                target = j
        if target != i:
            arr[i], arr[target] = arr[target], arr[i]
            count += 1
            if count == k:
                print(arr[target], arr[i])
                isFind = True
                break
    if isFind == False:
        print(-1)

if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().split())
    l = list(map(int, sys.stdin.readline().split()))
    sort(l)



