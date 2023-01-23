# [LeetCode] 937. Reorder Data in Log Files

생성일: 2022년 12월 7일 오전 4:15
수정 날짜: 2022년 12월 9일
태그: LeetCode, Medium, Python

You are given an array of `logs`. Each log is a space-delimited string of words, where the first word is the **identifier**.

There are two types of logs:

- **Letter-logs**: All words (except the identifier) consist of lowercase English letters.
- **Digit-logs**: All words (except the identifier) consist of digits.

Reorder these logs so that:

1. The **letter-logs** come before all **digit-logs**.
2. The **letter-logs** are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
3. The **digit-logs** maintain their relative ordering.

Return *the final order of the logs*.

**Example 1:**

```
Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
Explanation:
The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".

```

**Example 2:**

```
Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

```

**Constraints:**

- `1 <= logs.length <= 100`
- `3 <= logs[i].length <= 100`
- All the tokens of `logs[i]` are separated by a **single** space.
- `logs[i]` is guaranteed to have an identifier and at least one word after the identifier.

### 정답 코드

```python
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits
```

- 로그들을 문자 로그와 숫자 로그로 구분하기 위한 리스트 2개를 선언한다.
- logs를 순회하면서 log를 공백을 기준으로 나누어 로그의 시작 부분이 숫자이면 digits에 아니면, letters에 각각 추가한다.
- sort() 메서드를 이용하여 식별자를 제외한 문자열을 키로 설정하여 정렬하고, 문자열이 같은 경우 식별자를 키로하여 정렬한다.
- 정렬된 두 리스트를 병합하여 반환한다.

### isdigit() 함수

문자열이 숫자로 이루어져 있을 경우 True, 아니면 False를 반환한다.

### isalpha() 함수

문자열이 문자로만 이루어져 있을 경우 True, 아니면 False를 반환한다.

### isalnum() 함수

문자열이 문자와 숫자로 이루어져 있으면 True 아니면 False를 반환한다.