# [LeetCode] 42. Trapping Rain Water

생성일: 2022년 12월 12일 오후 11:50
태그: Hard, 구현, LeetCode, Python

### 문제

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

**Example 1:**

![https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png](https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png)

```
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
```

**Example 2:**

```
Input: height = [4,2,0,3,2,5]
Output: 9
```

**Constraints:**

- `n == height.length`
- `1 <= n <= 2 * 104`
- `0 <= height[i] <= 105`

### 1. 투 포인터를 이용한 해법

- 두 개의 포인터가 각각 리스트의 좌, 우에서 시작한다.
- 현재 포인터가 가리키고 있는 인덱스를 left, right에 저장하고, 포인터가 지나왔던 자리 중 가장 높았던 값을 left_max, right_max에  저장한다.
- 두 포인터가 만날 때까지 while문을 돌게 되는데, left_max와 right_max의 값을 매번 포인터가 이동할 때마다 해당 포인터의 자리의 높이와 비교를 해서 업데이트를 시킨다.
- left_max와 right_max 중 낮은 값을 가진 쪽의 포인터를 이동시킨다. 이 때 해당 위치에서 쌓이는 물을 그때그때 volume에 저장한다.
- left는 좌에서 우로, right는 우에서 좌로 이동하면서 결국 가장 높은 지점에서 두 포인터가 만나 끝이 나게 된다.

```python
class Solution:
    def trap(self, height: List[int]) -> int:
				# 인수로 받은 배열이 비어있을 경우
        if not height:
            return 0
        
        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            
            # 더 높은 쪽을 향해 투 포인터 이동
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume
```

### 2. 스택을 이용한 해법

```python
class Solution:
	# 풀이 2. 스택 쌓기
    # height를 스택에 쌓아 가다가 변곡점(현재 보다 높아질 때)을 기준으로 격차만큼 물 높이 volume을 채움
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
           # 변곡점을 만나는 경우
            while stack and height[i] > height[stack[-1]]:
                # 스택에서 꺼낸다
                top = stack.pop()

                if not len(stack):
                    break

                # 이전과의 차이만큼 물 높이 처리
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]
                volume += distance * waters

            stack.append(i)

        return volume
```