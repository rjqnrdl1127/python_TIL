import sys

def binary_search(arr, i):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if i == arr[mid]:
            return 1
        elif i < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return 0

if __name__ == '__main__':
    # 카드 개수 N
    n = int(sys.stdin.readline())
    # 상근이의 카드
    card = list(map(int, sys.stdin.readline().split()))
    # 찾을 카드 개수 M
    m = int(sys.stdin.readline())
    card2 = list(map(int, sys.stdin.readline().split()))
    card.sort()

    for i in card2:
        print(binary_search(card, i), end=' ')