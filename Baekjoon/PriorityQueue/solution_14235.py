import sys
import heapq

n = int(sys.stdin.readline())  # 방문 횟수 n
max_heap = [] # 선물의 가치 (최대 힙)

for _ in range(n):
    l = list(map(int, sys.stdin.readline().split()))
    count = l[0]

    if len(max_heap) == 0 and count == 0: # 힙이 비어있고 a가 0인 경우
        print(-1)
    elif l[0] == 0 and len(max_heap) != 0:  # 힙이 비어있지 않고 a가 0인 경우
        print(-1 * heapq.heappop(max_heap))  # 선물의 가치를 출력
    else:
        for i in range(1, count + 1):
            heapq.heappush(max_heap, -l[i]) # 선물의 가치를 최대 힙에 저장