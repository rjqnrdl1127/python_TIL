# [Python] re 모듈 사용법

생성일: 2022년 10월 20일 오전 6:58

# **[Python] re 모듈 사용법**

[언어/파이썬 & 장고](https://brownbears.tistory.com/category/%EC%96%B8%EC%96%B4/%ED%8C%8C%EC%9D%B4%EC%8D%AC%20%26%20%EC%9E%A5%EA%B3%A0) 2020. 7. 25. 22:53

regex는 정규 표현식으로 흔히 알려져 있습니다. 파이썬에서 정규 표현식을 사용할 때, 내장 모듈인 re를 사용하고 있습니다. re 모듈에서 제공해주는 함수들을 보면 match(), fullmatch(), findall(), search() 등등이 있는데 어떤 함수를 사용하냐에 따라 결과가 달라지게 됩니다. 여기서는 정규 표현식에 대한 기본부터 설명하는 것이 아닌, 파이썬의 re 모듈에서 제공하는 함수의 쓰임새를 예제와 함께 설명하여 사용자의 목적에 맞게 사용할 수 있도록 설명합니다.

# 왜 정규 표현식을 쓸까?

파이썬에서는 문자열에서도 기본적으로 특정 문자 또는 문자열이 존재하는지나 어느 위치에 있는지와 같은 기능을 제공합니다.

```
'123' in 'abc123def'
# True
s = 'foo123bar'
s.find('123')
# 3
s.index('123')
# 3
```

---

만약 문자열 안에 정수만 추출하고 싶다면 위 문자열에서 제공하는 함수만으로는 한계가 있습니다. 이럴 때, 정규 표현식을 사용하면 쉽게 찾을 수 있습니다.

```
import re

re.findall('\d+', 'abc123def56zz')
# ['123', '56']
```

---

# 메타문자

위에서 보는 것처럼 파이썬에는 특수한 기능을  하는 문자가 존재합니다. 이를 메타문자라고 하며 아래와 같이 존재합니다.

$()*+.?[]\^{}|

---

정규표현식에 a는 문자 a와 매칭되지만 (는 (와 매칭되지 않습니다. 메타문자인 소괄호인 (를 매칭하고자 하면 백슬래쉬인 \를 앞에 붙여 \( 라 작성해야 문자 (와 매칭이 가능합니다. 이에 관한 설명은 [https://brownbears.tistory.com/62](https://brownbears.tistory.com/62) 에서 확인할 수 있습니다.

# re 모듈의 함수

## match(패턴, 문자열, 플래그)

match()는 문자열의 처음부터 시작해서 작성한 패턴이 일치하는지 확인합니다.

```
import re

print(re.match('a', 'ab'))
print(re.match('a', 'ab'))
print(re.match('a', 'bba'))
print(re.match('a', 'ba'))

# <re.Match object; span=(0, 1), match='a'>
# <re.Match object; span=(0, 1), match='a'>
# None
# None
```

---

예시의 1,2번의 시작은 a로 시작하여 매칭이 된 것으로 확인되는데 3,4번은 시작이 b로 시작하므로 매칭이 안 된 것을 확인할 수 있습니다.

## search(패턴, 문자열, 플래그)

search()는 match()와 유사하지만 패턴이 문자열의 처음부터 일치하지 않아도 괜찮습니다.

```
import re

print(re.search('a', 'ab'))
print(re.search('a', 'ab'))
print(re.search('a', 'bba'))
print(re.search('a', 'ba'))

# <re.Match object; span=(0, 1), match='a'>
# <re.Match object; span=(0, 1), match='a'>
# <re.Match object; span=(2, 3), match='a'>
# <re.Match object; span=(1, 2), match='a'>
```

---

패턴과 일치만 한다면 문자열의 시작과는 상관없이 전부 찾아서 결과를 반환해 줍니다. 아마도 정규식을 사용한다면 해당 함수를 가장 많이 사용할 것 같습니다.

## findall(패턴, 문자열, 플래그)

findall()은 문자열 안에 패턴에 맞는 케이스를 전부 찾아서 리스트로 반환합니다.

```
import re

print(re.findall('a', 'a'))
print(re.findall('a', 'aba'))
print(re.findall('a', 'baa'))
print(re.findall('aaa', 'aaaaa'))
print(re.findall('aaa', 'aaaaaa'))
print(re.findall('\d', '숫자123이 이렇게56 있다8'))
print(re.findall('\d+', '숫자123이 이렇게56 있다8'))

# ['a']
# ['a', 'a']
# ['a', 'a']
# ['aaa']
# ['aaa', 'aaa']
# ['1', '2', '3', '5', '6', '8']
# ['123', '56', '8']

```

---

4번째 예시를 보면 패턴은 aaa이고 문자열은 aaaaa 5개입니다. 해당 함수는 겹치는 것을 제공하지 않으므로 aaa를 3개를 보여주는 형태가 아닌 1개만 보여주게 됩니다. 5번째의 예시는 a가 6개 이므로 패턴에 해당하는 문자열이 2개가 존재하여 aaa를 2번 리스트에 담아 반환합니다.

## finditer(패턴, 문자열, 플래그)

findall()과 유사하지만 패턴에 맞는 문자열의 리스트가 아닌 iterator 형식으로 반환합니다.

```
import re

re_iter = re.finditer('a', 'baa')
for s in re_iter:
    print(s)

# <re.Match object; span=(1, 2), match='a'>
# <re.Match object; span=(2, 3), match='a'>
```

---

해당 함수를 사용하는 목적은 패턴에 맞는 문자열과 어느 위치에 존재 하는지를 확인할 때 사용할 수 있습니다.

## fullmatch(패턴, 문자열, 플래그)

fullmatch()는 문자열에 시작과 끝이 정확하게 패턴과 일치할 때 반환합니다. match()는 처음부터 패턴에 맞으면 반환을 하지만 해당 함수는 시작과 끝이 정확하게 일치해야 합니다.

```
import re

print(re.fullmatch('a', 'a'))
print(re.fullmatch('a', 'aaa'))
print(re.fullmatch('a', 'ab'))
print(re.fullmatch('a', 'ba'))
print(re.fullmatch('a', 'baa'))

# <re.Match object; span=(0, 1), match='a'>
# None
# None
# None
# None
```

---

## split(패턴, 문자열, 최대 split 수, 플래그)

split은 문자열에서 패턴이 맞으면 이를 기점으로 리스트로 쪼개는 함수입니다. 만약 3번째 인자(최대 split 수)를 지정하면 문자열을 지정한 수 만큼 쪼개고 그 수가 도달하면 쪼개지 않습니다.

```
import re

print(re.split('a', 'abaabca'))
print(re.split('a', 'abaabca', 2))

# ['', 'b', '', 'bc', '']
# ['', 'b', 'abca']
```

---

## sub(패턴, 교체할 문자열, 문자열, 최대 교체 수, 플래그)

sub는 문자열에 맞는 패턴을 2번째 인자(교체할 문자열)로 교체합니다. split의 최대 split 수와 동일하게 최대 교체 수를 지정하면 문자열에 맞는 패턴을 교체할 문자열로 교체하고 그 수가 도달하면 더이상 교체하지 않습니다.

```
import re

print(re.sub('a', 'z', 'ab'))
print(re.sub('a', 'zxc', 'ab'))
print(re.sub('a', 'z', 'aaaab'))
print(re.sub('a', 'z', 'aaaab', 1))

# zb
# zxcb
# zzzzb
# zaaab
```

---

## subn(패턴, 교체할 문자열, 문자열, 최대 교체 수, 플래그)

sub()와 동작은 동일하지만 반환 결과가 결과 (문자열, 매칭횟수) 형태로 반환됩니다.

```
import re

print(re.subn('a', 'z', 'ab'))
print(re.subn('a', 'zxc', 'ab'))
print(re.subn('a', 'z', 'aaaab'))
print(re.subn('a', 'z', 'aaaab', 1))

# ('zb', 1)
# ('zxcb', 1)
# ('zzzzb', 4)
# ('zaaab', 1)
```

---

## compile(패턴, 플래그)

만약 패턴과 플래그가 동일한 정규식을 여러번 사용하려면 compile()를 사용하여 지정한 다음, 위의 함수들을 사용할 수 있습니다.

```
import re

c = re.compile('a')

print(c.sub('zxc', 'abcdefg'))
print(c.search('vcxdfsa'))

# zxcbcdefg
# <re.Match object; span=(6, 7), match='a'>
```

---

## purge()

위 complie()로 만들어 놓은 객체는 캐시에 보통 100개까지 저장된다고 알려져 있으며 그 수를 넘어가면 초기화 됩니다. purge()를 호출하면 100개가 넘어가지 않아도 캐시를 초기화 하는 함수입니다.

```
import re

re.purge()
```

---

## escape(패턴)

escape()는 패턴을 입력 받으면 특수문자들에 이스케이프(백슬래쉬) 처리를 한 다음 반환합니다.

```
import re

print(re.escape('(\d)'))

# \(\\d\)
```

---

## match object method()

findall()를 제외하고 모든 함수들의 반환은 match object로 반환됩니다. match object에서는 group(), start(), end() 등과 같이 찾은 패턴이 문자열의 위치나 매칭 문자열을 반환하는 함수를 제공합니다.

### **group(), start(), end(), span()**

예를 들어 search()로 패턴에 맞는 문자열을 찾았다 하면 group() 메서드를 통해 패턴에 맞는 문자열을 추출할 수 있고, start()를 사용해 문자열에서 어디부터 패턴에 맞는 문자가 시작했는지, end()를 통해 어디까지인지, span()으로 어디부터 어디까지인지 확인할 수 있습니다.

```
import re

result = re.search('aa', 'baab')
print(result.group())
print(result.start())
print(result.end())
print(result.span())

# aa
# 1
# 3
# (1, 3)
```

---

### **groups(), group(int)**

만약 위와 같이 단순한 형태가 아닌, 소괄호 ()를 사용해 패턴을 묶어 찾는다면 아래와 같이 groups()와 group(int)를 사용할 수 있습니다.

```
import re

result = re.match('(\d{2})-(\d{3,4})-(\d{4})', '02-123-1234')
print(result.groups())
print(result.group())
print(result.group(0))
print(result.group(1))
print(result.group(2))

# ('02', '123', '1234')
# 02-123-1234
# 02-123-1234
# 02
# 123
```

---

소괄호를 사용해 패턴을 체크하고 체크한 값을 변수로 저장해야만 위의 함수들을 사용할 수 있습니다. 아래는 소괄호를 전부 제거한 패턴인데 결과는 동일하지만 groups()를 사용하지 못하는 모습입니다.

```
import re

result2 = re.match('\d{2}-\d{3,4}-\d{4}', '02-123-1234')
print(result2.groups())
print(result2.group())

# ()
# 02-123-1234
```

---

### **groupdict()**

groupdict()를 사용하려면 패턴에 맞는 결과에 이름을 주어야만 합니다. 패턴에 이름을 주려면 (?P<이름>) 형식이 되어야만 합니다. 여기서도 소괄호가 존재하지 않으면 에러가 발생합니다.

```
import re

result = re.match('(?P<front>\d{2})-(?P<middle>\d{3,4})-(?P<rear>\d{4})', '02-123-1234')

print(result.groupdict())
print(result.groups())
print(result.group(1))
print(result.group('front'))

# {'front': '02', 'middle': '123', 'rear': '1234'}
# ('02', '123', '1234')
# 02
# 02
```

---

## 패턴

위 함수들의 가장 마지막 인자에는 패턴을 추가할 수 있으며 re모듈은 아래와 같은 패턴을 지원합니다.

I, IGNORECASE: 대소문자 구분 X

L, LOCATE: \w, \W, \b, \B를 현재의 로케일에 영향을 받음

M, MULTILINE: 여러 줄의 문자열에 대해 패턴을 탐색할 수 있게 함

S, DOTALL: .을 줄바꾸기 문자도 포함하여 매치하게 함

U, UNICODE: \w, \W, \b, \B가 유니코드 문자 특성에 의존함

X, VERBOSE: 정규식 안의 공백 무시

위의 패턴은 아래와 같이 사용할 수 있으며 여러 패턴을 등록하려면 | 을 사용합니다.

```
import re

s = """
c
b
A
"""
print(re.search('a', s, re.M|re.I))

# <re.Match object; span=(5, 6), match='A'>
```

---