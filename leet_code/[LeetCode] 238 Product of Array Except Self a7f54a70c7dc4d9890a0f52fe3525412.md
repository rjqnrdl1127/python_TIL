# [LeetCode] 238. Product of Array Except Self

생성일: 2022년 12월 14일 오전 1:09
태그: 구현, LeetCode, Medium, Python

[Product of Array Except Self - LeetCode](https://leetcode.com/problems/product-of-array-except-self/)

### 난이도: Medium

Given an integer array `nums`, return *an array* `answer` *such that* `answer[i]` *is equal to the product of all the elements of* `nums` *except* `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

**Example 1:**

```
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

```

**Example 2:**

```
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

```

**Constraints:**

- `2 <= nums.length <= 105`
- `30 <= nums[i] <= 30`
- The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

**Follow up:** Can you solve the problem in `O(1)` extra space complexity? (The output array **does not** count as extra space for space complexity analysis.)

### 1. 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈

- 왼쪽부터 곱해서 result에 추가한다.
- 왼쪽의 곱셈 결과에 오른쪽 마지막 값부터 차례대로 곱해 나간다.
- p는 1부터 차례대로 커지면서 4, 12, 24가 되고, 최종적으로 이 값이 왼쪽 곱셈 결과에 곱해져 [24, 12, 8, 6]이 된다.

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        p = 1
        # 왼쪽 곱셈
        for i in range(len(nums)):
            out.append(p)
            p = p * nums[i]
        
        p = 1
        #왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
        for i in range(len(nums) - 1, 0 - 1, -1):
            out[i] = out[i] * p
            p = p * nums[i]

        return result
```

### 2. 중첩 for문을 이용한 부루트 포스(타임 아웃)

- 주어진 리스트에서 0부터 n번째 값까지 각각의 원소를 제거 후 곱한 결과를 result에 저장
- 반복문이 끝난 후 리스트를 반환한다.

이 풀이는 문제를 단순하게 접근했을 때의 풀이로 O(n^2)의 시간 복잡도를 가지기 때문에 결국에는 타임 아웃이 되었다. 하지만 Example 1, 2는 통과하였다.

제약 사항을 꼼꼼히 읽어보면 시간 복잡도가 O(n^2)이 나오면 안된다는 것을 알 수 있다.

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
				
        for i, n in enumerate(nums):
            mul = 1
						# 배열의 n번째 원소를 제거 후 곱한값을 리스트에 저장
            nums.remove(n)
            for x in nums:
                mul *= x
            result.append(mul)
						# 원래 인덱스에 다시 추가
            nums.insert(i, n)
        return result
```