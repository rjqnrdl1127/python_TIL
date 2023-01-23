from typing import List
import heapq


#in place memory sorting
def heapSort(nums:List[int])->List[int]:
    #python does not have maxHeap. multiply by -1
    nums = [-1*n for n in nums]
    heapq.heapify(nums)

    sorted = [0] * len(nums)

    for i in range(len(nums)-1,-1,-1):
        largest = -1 * heapq.heappop(nums)
        sorted[i] = largest
    return sorted