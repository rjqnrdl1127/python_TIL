# [LeetCode]9. Palindrome Number

생성일: 2022년 11월 20일 오후 11:40
수정 날짜: 2022년 12월 9일
태그: Easy, 구현, LeetCode, Python

[Palindrome Number - LeetCode](https://leetcode.com/problems/palindrome-number/)

### 난이도 : **Easy**

Given an integer `x`, return `true` *if* `x` *is a **palindrome**, and* `false` *otherwise*.

부호가 있는 숫자가 문자열로 주어질 경우, 문자열을 거꾸로 했을 때와 원래 문자열이 같다면 true 아니면 false를 반환

**Example 1:**

```
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

```

**Example 2:**

```
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

```

**Example 3:**

```
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

```

**Constraints:**

- `231 <= x <= 231 - 1`

**Follow up:**

Could you solve it without converting the integer to a string?

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]: # 문자열로 변환한 x와 그것을 거꾸로한 문자열을 비교 
            return True
        return False
```