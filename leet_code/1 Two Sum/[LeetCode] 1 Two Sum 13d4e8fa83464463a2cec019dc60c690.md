# [LeetCode] 1. Two Sum

생성일: 2022년 11월 20일 오후 11:11
수정 날짜: 2022년 12월 12일
태그: Easy, 구현, LeetCode, Python

[Two Sum - LeetCode](https://leetcode.com/problems/two-sum/)

### 난이도 : Easy

## 문제

Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.

You may assume that each input would have ***exactly* one solution**, and you may not use the *same* element twice.

You can return the answer in any order.

숫자 리스트 nums에서 합이 target인 두 수를 리스트에 담아서 반환

**Example 1:**

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

```

**Example 2:**

```
Input: nums = [3,2,4], target = 6
Output: [1,2]

```

**Example 3:**

```
Input: nums = [3,3], target = 6
Output: [0,1]

```

**Constraints:**

- `2 <= nums.length <= 104`
- `109 <= nums[i] <= 109`
- `109 <= target <= 109`
- **Only one valid answer exists.**

**Follow-up:**

Can you come up with an algorithm that is less than

$$
O(n^2)
$$

time complexity?

### 1. 부루트 포스 풀이

부르트 포스는 무차별 대입 방식으로, 배열의 인덱스 2개를 접근하여 값을 더해보고 target과 같다면 배열에 담아 return한다.

최선의 경우 O(1)에 답을 찾을 수 있지만, 최악의 경우 O(n^2)까지 시간 복잡도가 증가한다.

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
				# 뒤에서 부터 앞으로 인덱스를 옮기며 합을 구한다
        for i in range(len(nums) - 1, -1, -1):
            for j in range(len(nums) - 1, i, -1):
                if target == (nums[i] + nums[j]): # 합이 target일 경우 리스트 리턴
                    result = [i, j]
                    return result
                    break
```

![스크린샷 2022-12-12 오후 11.39.31.png](%5BLeetCode%5D%201%20Two%20Sum%2013d4e8fa83464463a2cec019dc60c690/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2022-12-12_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_11.39.31.png)

### 2. in을 이용한 탐색

 모든 조합을 비교하지 않고 정답, 즉 타겟에서 첫 번째 값을 뺀 값 target - n이 존재하는지 탐색하는 문제로 변경하면,

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n

            if complement in nums[i + 1:]:
                return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]
```

nums가  {2,7,11,15}고 target이 9라면 배열의 첫 번째 수를 뺀 7이 배열에 존재하는지 확인하고 있다면 7의 인덱스를 배열에 담아 return한다. 부르트 포스보다 훨씬 빠른 속도로 답을 찾을 수 있다.

![스크린샷 2022-12-12 오후 11.39.50.png](%5BLeetCode%5D%201%20Two%20Sum%2013d4e8fa83464463a2cec019dc60c690/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2022-12-12_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_11.39.50.png)

### 3. 딕셔너리를 이용한 탐색

딕셔너리에 값을 키로하고 인덱스를 값으로 하여 저장한 후 합이 target이 되는 두 수를 찾을 수 있다.

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
				# {2: 0, 7: 1, 11: 2, 15: 3}으로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i
        
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [i, nums_map[target - num]]
```

딕셔너리 자료형을 사용하면 target - n의 인덱스를 찾는데 O(1)만큼의 시간이 걸리기 때문에 in을 이용한 탐색보다 빠르게 값을 찾을 수 있다. 하지만 아직 for문이 두 번 사용 되기 때문에 이 방법은 최선이 아니다.

![스크린샷 2022-12-12 오후 11.40.02.png](%5BLeetCode%5D%201%20Two%20Sum%2013d4e8fa83464463a2cec019dc60c690/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2022-12-12_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_11.40.02.png)

### 4. 딕셔너리를 이용한 탐색(for문 1개)

위 코드를 좀 더 간결하게 해보면,

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i
```

for문 하나로 딕셔너리에 값을 추가하는 것과 두 수를 찾는 것을 동시에 시행할 수 있다. 만약 조건에 맞는 두 수를 찾으면 배열에 담아서 return한다. 이전 방식은 딕셔너리에 값을 모두 추가한 후 두 수를 찾은 반면, 이번에는 값을 추가하고 추가한 값을 target에서 뺀 값이 딕셔너리에 있는지 확인하고 있으면 두 수의 인덱스를 배열에 담아 반환한다. 따라서 인수로 받은 배열의 모든 값을 딕셔너리에 추가하기 전에 답을 찾으면 답을 반환한다.

![스크린샷 2022-12-12 오후 11.40.17.png](%5BLeetCode%5D%201%20Two%20Sum%2013d4e8fa83464463a2cec019dc60c690/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2022-12-12_%25E1%2584%258B%25E1%2585%25A9%25E1%2584%2592%25E1%2585%25AE_11.40.17.png)

### 결론

이번 문제는 리트코드의 첫 문제로 매우 쉬운 문제였다. 문제 이해에는 어려움이 없었지만, 시간 복잡도를 줄이기 위해서 다양한 시도를 해보았다. 브루트 포스로도 해결할 수 있었지만, 해시 테이블(딕셔너리) 자료구조를 이용하여 원하는 값을 찾을 때 빠르다는 것을 느꼈다. 파이썬 내장 함수인 enumerate()에 대해서도 확실히 이해 되었다.