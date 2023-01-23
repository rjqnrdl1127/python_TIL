import sys
import heapq

n = int(sys.stdin.readline())

heap = []

for _ in range(n):
    list = [int(i) for i in sys.stdin.readline().split()]

    if not heap: # 힙이 비어 있는 경우
        for a in list: # 표의 첫 번째 줄을 min-heap에 추가
            heapq.heappush(heap, a)
    else: # 힙이 비어 있지 않는 경우
        for a in list: # 두 번째 줄에 있는 숫자를
            if heap[0] < a: # min-heap의 루트와 비교해서 루트보다 큰 경우
                heapq.heappush(heap, a) # 힙에 추가
                heapq.heappop(heap) # 루트는 제거

print(heap[0]) # 모든 숫자를 비교 후 힙의 루트를 출력(n번째로 큰 수)