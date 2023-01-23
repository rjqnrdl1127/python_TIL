import sys
input = sys.stdin.readline

def get_parent(parent, a):
    if parent[a] != a:
        parent[a] = get_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a_p, b_p):
    if a_p < b_p:
        parent[b_p] = a_p
    else:
        parent[a_p] = b_p

if __name__ == '__main__':
    n, m = map(int, input().split())
    parent = [i for i in range(0, n + 1)]
    edges = []
