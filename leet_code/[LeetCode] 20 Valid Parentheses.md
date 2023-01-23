# [LeetCode] 20. Valid Parentheses

생성일: 2022년 11월 21일 오전 9:54
수정 날짜: 2022년 12월 9일
태그: Easy, 구현, LeetCode, Python

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

**Example 1:**

```
Input: s = "()"
Output: true

```

**Example 2:**

```
Input: s = "()[]{}"
Output: true

```

**Example 3:**

```
Input: s = "(]"
Output: false

```

**Constraints:**

- `1 <= s.length <= 104`
- `s` consists of parentheses only `'()[]{}'`.

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        brackets={'}':'{',')':'(',']':'['}
        for bracket in s:
            if bracket in brackets.values(): #Opening bracket 
                stack.append(bracket)
            else:# Closing bracket
                if stack and brackets[bracket]==stack[-1] :  
                    stack.pop()
                else: 
                    return False
        
        if stack:
            return False
        return True
```