# [LeetCode] 14. Longest Common Prefix

생성일: 2022년 11월 21일 오전 3:15
수정 날짜: 2022년 12월 9일
태그: Easy, 구현, LeetCode, Python

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

**Example 1:**

```
Input: strs = ["flower","flow","flight"]
Output: "fl"

```

**Example 2:**

```
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

```

**Constraints:**

- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` consists of only lowercase English letters.

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=[]
        num = len(strs)
        for x in zip(*strs):
            if len(set(x)) == 1:
                prefix.append(x[0])
            else:
                break
                
        return "".join(prefix)
```

[Longest Common Prefix - LeetCode](https://leetcode.com/problems/longest-common-prefix/)