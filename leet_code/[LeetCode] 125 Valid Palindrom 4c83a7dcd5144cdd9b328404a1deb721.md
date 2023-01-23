# [LeetCode] 125. Valid Palindrom

생성일: 2022년 12월 7일 오전 3:36
수정 날짜: 2022년 12월 9일
태그: Easy, LeetCode, Python

## 문제

주어진 문자열이 팰린드롬인지 확인 하라. 대소문자를 구분하지 않으며 영문자와 숫자만을 대상으로 한다.

**Example 1:**

```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

```

**Example 2:**

```
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

```

**Example 3:**

```
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

```

**Constraints:**

- `1 <= s.length <= 2 * 105`
- `s` consists only of printable ASCII characters.

## 1. 리스트로 변환

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
				# isalnum() 함수로 숫자와 영문자 여부 판별하여 리스트에 저장
        for i in s:
            if i.isalnum():
                strs.append(i.lower())
        # 리스트의 맨 앞과 맨 뒤의 문자를 서로 비교하여 같지 않으면 False 리턴
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        
        return True
```

- isalnum() 함수는 영문자, 숫자 여부를 판별하는 함수로, 이를 이용해 해당하는 문자만 추가한다.
- pop() 함수는 리스트의 맨 뒤 요소를 반환한 후 리스트에서 제거한다.
- pop() 함수에 인덱스를 정해주면 해당 인덱스의 요소를 반환한 후 리스트에서 제거한다.

## 2. 데크를 이용한 최적화

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs: Deque = collections.deque()
        for i in s:
            if i.isalnum():
                strs.append(i.lower())
        # deque의 popleft() 함수를 이용하여 맨 앞의 문자에 접근
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        
        return True
```

- deque() 함수는 데크 자료형을 생성하는 함수이다.
- popleft() 함수는 데크의 맨 앞 요소를 반환한 후 데크에서 제거한다.(리스트의 pop(0) 함수와 동일)
- 데크의 popleft() 함수는 리스트의 pop() 함수보다 시간 복잡도가 낮다.

## 3. 문자열 슬라이싱 사용

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
				# 소문자로 통일
        s = s.lower()
				# 정규식으로 특수문자 제거
        s = re.sub('[^a-z0-9]', '', s)
				# 슬라이싱으로 원래 문자열과 역순 문자열을 비교하고 결과 리턴
        return s == s[::-1]
```

- s[::-1]은 문자열을 빠르고 쉽게 뒤집을 수 있는 방법 중 하나이다.
- 슬라이싱을 사용하면 위 두 방법보다 훨씬 빠르게 로직을 수행한다.

| 구분 | 리스트 | 데크 | 슬라이싱 |
| --- | --- | --- | --- |
| 시간 | 689ms | 87ms | 78ms |
| 메모리 | 19.3MB | 19.3MB | 15.5MB |

## 결론

문자열을 조작해야 할 때는 파이썬에서 제공하는 슬라이싱 같은 기능들을 적극적으로 활용하는 것이 좋다.

문자열을 배열처럼 인덱스로 접근하는 파이썬 특성상 굳이 리스트나 데크 자료형으로 바꾸어 접근할 필요가 없다는 것을 깨달았다.

[Valid Palindrome - LeetCode](https://leetcode.com/problems/valid-palindrome/description/)