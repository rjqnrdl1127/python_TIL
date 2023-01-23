import sys

if __name__ == '__main__':
    input = sys.stdin.readline()
    s = list(input.strip())
    answer = []
    tmp = []

    for i in range(1, len(s) - 1):
        for j in range(i + 1, len(s)):
            a = s[:i]
            b = s[i:j]
            c = s[j:]
            a.reverse()
            b.reverse()
            c.reverse()
            tmp.append(a + b + c)

    for a in tmp:
        answer.append(''.join(a))

    print(sorted(answer)[0])