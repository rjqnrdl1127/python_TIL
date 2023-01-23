# [LeetCode] 561. Array Partition

생성일: 2022년 12월 14일 오전 12:31
태그: Easy, 구현, LeetCode, Python

[Array Partition - LeetCode](https://leetcode.com/problems/array-partition/description/)

### 난이도: Easy

Given an integer array `nums` of `2n` integers, group these integers into `n` pairs `(a1, b1), (a2, b2), ..., (an, bn)` such that the sum of `min(ai, bi)` for all `i` is **maximized**. Return *the maximized sum*.

**Example 1:**

```
Input: nums = [1,4,3,2]
Output: 4
Explanation: All possible pairings (ignoring the ordering of elements) are:
1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
So the maximum possible sum is 4.
```

**Example 2:**

```
Input: nums = [6,2,6,5,1,2]
Output: 9
Explanation: The optimal pairing is (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9.

```

**Constraints:**

- `1 <= n <= 104`
- `nums.length == 2 * n`
- `104 <= nums[i] <= 104`

### 1. 오름차순 풀이

 문제가 상당히 특이하고 바로 이해하기 어려웠다. 하지만 천천히 읽어보니 페어의 min()을 합산했을 때 최대를 만드는 것으로, 결국 min()이 되도록 커야 한다는 뜻이고, 뒤에서부터 내림차순으로 집어넣으면 항상 최대 min() 페어를 유지할 수 있다. 

- min(1, 4) + min(2, 3) = 3
- min(1, 3) + min(2, 4) = 3
- min(1, 2) + min(3, 4) = 4

Example 1에서 만들 수 있는 경우의 수는 3가지이고, 세 번째 경우처럼 배열이 정렬된 상태에서 앞에서붵 오름차순으로 페어를 만들면 된다. 뒤에서부터 내림차순으로 페어를 만들어도 결과는 동일하다.

```python
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        pair = []
				# 배열을 오름차순으로 정렬
        nums.sort()

        for n in nums:
						# 앞에서부터 오름차순으로 페어를 만들어서 합 계산
            pair.append(n)
            if len(pair) == 2:
                sum += min(pair)
                pair = []

        return sum
```

### 2. 짝수 번째 값 계산

위 방법 이외에 정렬된 배열의 짝수 번째 값을 더하면 된다. 배열을 오름차순으로 정렬하면 페어로 만들었을 때 작은 값이 짝수 인덱스에 위치하게 된다. 위 코드를 약간만 수정해 주면 된다.

```python
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        pair = []
				# 배열을 오름차순으로 정렬
        nums.sort()

        for i, n in enumerate(nums):
						# 짝수 번째 값의 합 계산
            if i % 2 == 0:
                sum += min(pair)
                pair = []

        return sum
```

위 코드를 파이썬의 내장함수를 이용하면 한 줄로 정리 할 수 있다.

```python
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
```