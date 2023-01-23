def selection_sort(arr):
    # 중첩 반복문으로 O(N^2)의 시간 복잡도
    for i in range(len(arr) - 1):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], min[i] # 자리 바꿈
