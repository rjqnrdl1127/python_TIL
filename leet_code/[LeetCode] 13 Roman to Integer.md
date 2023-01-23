# [LeetCode] 13. Roman to Integer

생성일: 2022년 11월 21일 오전 12:05
수정 날짜: 2022년 12월 9일
태그: Easy, 구현, LeetCode, Python

### 난이도 : Easy

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

```
SymbolValue
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

For example, `2` is written as `II` in Roman numeral, just two ones added together. `12` is written as `XII`, which is simply `X + II`. The number `27` is written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

- `I` can be placed before `V` (5) and `X` (10) to make 4 and 9.
- `X` can be placed before `L` (50) and `C` (100) to make 40 and 90.
- `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

**Example 1:**

```
Input: s = "III"
Output: 3
Explanation: III = 3.

```

**Example 2:**

```
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

```

**Example 3:**

```
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

```

**Constraints:**

- `1 <= s.length <= 15`
- `s` contains only the characters `('I', 'V', 'X', 'L', 'C', 'D', 'M')`.
- It is **guaranteed** that `s` is a valid roman numeral in the range `[1, 3999]`.

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0 # 정답 변수
        st = dict() # 로마 숫자를 딕셔너리로 저장
        st['I'] = 1
        st['V'] = 5
        st['IV'] = 4
        st['X'] = 10
        st['IX'] = 9
        st['L'] = 50
        st['XL'] = 40
        st['C'] = 100
        st['XC'] = 90
        st['D'] = 500
        st['CD'] = 400
        st['M'] = 1000
        st['CM'] = 900
        
        index = 0 # 문자열 인덱스
        
        while index != len(s) - 1:
						# 인덱스가 문자열 길이를 벗어나지 않으면서 두 자리 문자열이 딕셔너리에 있을 경우
            if index + 1 <= len(s) - 1 and (s[index] + s[index + 1]) in st.keys():
                answer += st[s[index] + s[index + 1]]
                index += 2
						# 인덱스가 문자열 길이를 벗어나지 않으면서 1개의 문자가 딕셔너리에 있을 경우
            elif index != len(s) and s[index] in st.keys():
                answer += st[s[index]]
                index += 1
            else:
                break
				# 인덱스가 마지막 문자일 경우
        if index == len(s) - 1:
            answer += st[s[index]]
        return answer # 정답 반환
```