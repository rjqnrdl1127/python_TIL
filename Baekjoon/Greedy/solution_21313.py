import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    ans = [1, 2] * (n // 2) + ([3] if n % 2 else [])
    print(*ans)