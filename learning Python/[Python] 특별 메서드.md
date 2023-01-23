# [Python] 특별 메서드

생성일: 2022년 10월 20일 오전 6:58
태그: python, 전문가를 위한 파이썬

## 특별 메서드는 어떻게 사용되나?

특별 메서드에 대해 먼저 알아두어야 할 점은, 이 메서드는 여러분이 아니라 파이썬 인터프리터가 호출하기 위한 것이라는 점이다. 객체를 만들 때, 특별 메서드를 구현해 놓으면 사용자는 __len__()으로 직접 호출하는 것ㅇ 아니라 len() 함수를 이용하여 호출한다. 이 때 파이썬 인터프리터가 len() 함수를 읽어서 __len__() 객체 메서드를 호출한다.

종종 특별 메서드가 암묵적으로 호출된다. 예를 들어 for i in x: 문의 경우 실제로는 iter(x)를 호출하며, 이 함수는 다시 x.__iter__()를 호출한다.

특별 메서드가 필요하다면 일반적으로 len(), str(), iter()와 같은 내장 함수를 호출하는 것이 좋다. 이들 내장 함수가 해당 특별 메서드를 호출한다.

### 수치형 흉내 내기

```python
from math import hypot

class Vector:

    def __init__(self, x=0, y=0): # 객체 생성자 메서드
        self.x = x
        self.y = y

    def __repr__(self): # 객체를 문자열로 표현하기 위한 특별 메서드
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
```

### 문자열 표현

__**repr**__() 특별 메서드는 객체를 문자열로  표현하기 위해 repr() 내장 메서드로 호출된다. __**repr**__() 메서드가 반환한 문자열은 명확해야 하며, 가능하면 표현된 객체를 재생성하는 데 필요한 소스 코드와 일치해야 한다. 

__**str**__() 메서드는 str() 생성자에 의해 호출되며 print() 함수에 의해 암묵적으로 사용된다. __str__()은 사용자에게 보여주기 적당한 형태의 문자열을 반환해야 한다.

__repr__()와 __str__() 중 하나만 구현해야 한다면, __repr__() 메서드를 구현하라. 파이썬 인터프리터는 __str__() 메서드가 구현되어 있지 않을 때의 대책으로 __repr__() 메서드를 호출하기 때문이다.

### 사용자 정의형의 불리언 값

__bool__()이나 __len__()을 구현하지 않을 경우, 기본적으로 사용자 정의 클래스의 객체는 참된 값이라고 간주된다. __bool__()이 구현되지 않으면 파이썬은 __len__()을 호출하며, 이 특별 메서드가 0을 반환하면 bool()은 False를, 그렇지 않으면 True를 반환한다.

위에 구현한 Vector의 __bool__()은 벡터의 크기가 0이면 False를 반환하고 그렇지 않으면 True를 반환한다. 불리언 값으로 반환해야 하기 때문에 bool(abs(self))를 이용해서 크기를 불리언형으로 반환한다.

### 특별 메서드 종류

| 문자열/바이트 표현 | repr, str, format, bytes |
| --- | --- |
| 숫자로 변환 | abs, bool, complex, int, float, hash, index |
| 컬렉션 애뮬레이션 | len, geitem, setitem, delitem, contains |
| 반복 | iter, reversed, next |
| 콜러블 애뮬레이션 | call |
| 콘텍스트 관리 | enter, exit |
| 객체 생성 및 소멸 | new, init, del |
| 속성 관리 | getattr, getattribute, setattr, delattr, dir |
| 속성 디스크립터 | get, set, delete |
| 클래스 서비스 | prepare, instancecheck, subclasscheck |

## 왜 len()은 메서드가 아닐까?

len(x)는 x가 내장형 객체일 때 아주 빨리 실행된다고 설명하였다. CPython의 내장 객체에 대해서는 메서드를 호출하지 않고 단지 C 언어 구조체의  필드를 읽어올 뿐이다. 컬렉션에 들어 있는 항목 수를 가져오는 연산은 자주 발생하므로 str, list, memoryview 등의 다양한 기본형 객체에 대해 효율적으로 작동해야 한다.

다시 말해, len()은 abs()와 만찬가지로 파이썬 데이터 모델에서 특별한 대우를 받으므로 메서드라고 부르지 않는다. 그러나 __len__() 특별 메서드 덕분에 여러분이 정의한 객체에서 len() 메서드를 직접 정의할 수 있다. 이것은 내장형 객체의 효율성과 언어의 일관성 간의 타협점을 어느 정도 찾은 것이다.

### 요약

특별 메서드를 구현하면 사용자 정의 클래스를 통해 만든 객체도 내장형 객체처럼 작동하게 되어, 파이썬다운 표현력 있는 코딩 스타일을 구사할 수 있다.

파이썬 객체는 기본적으로 자신을 문자열 형태로 제공해야 하는데, 디버깅 및 로그에 사용하는 형태와 사용자에게 보여주기 위해 형태가 있다. 그렇기 때문에 데이터 모델에 __repr__()과 __str__() 특별 메서드가 있는 것이다.

### 참고 자료

[전문가를 위한 파이썬 | 루시아누 하말류 - 교보문고](https://product.kyobobook.co.kr/detail/S000001057838)