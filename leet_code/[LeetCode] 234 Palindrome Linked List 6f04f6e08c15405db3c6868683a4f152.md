# [LeetCode] 234. Palindrome Linked List

생성일: 2022년 12월 14일 오전 4:12
태그: Easy, LeetCode, Python, 연결 리스트

Given the `head` of a singly linked list, return `true` *if it is a*

*palindrome*

*or*

```
false
```

*otherwise*

.

**Example 1:**

![https://assets.leetcode.com/uploads/2021/03/03/pal1linked-list.jpg](https://assets.leetcode.com/uploads/2021/03/03/pal1linked-list.jpg)

```
Input: head = [1,2,2,1]
Output: true

```

**Example 2:**

![https://assets.leetcode.com/uploads/2021/03/03/pal2linked-list.jpg](https://assets.leetcode.com/uploads/2021/03/03/pal2linked-list.jpg)

```
Input: head = [1,2]
Output: false

```

**Constraints:**

- The number of nodes in the list is in the range `[1, 105]`.
- `0 <= Node.val <= 9`

**Follow up:**

Could you do it in

```
O(n)
```

time and

```
O(1)
```

space?

### 1. 리스트로 변환

```python
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q: List = []

        if not head:
            return True
        
        node = head
        while node is not None:
            q.append(node.val)
            node = node.next
        
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False
        
        return True
```

### 2. 런너를 이용한 해법

### **런너(Runner) 기법**

- 런너 기법이란 **연결 리스트 순회 시** **2개의 포인터를 동시에 사용**하는 기법이다. 한 포인터가 다른 포인터보다 앞서게 하여 병합 지점이나 중간 위치, 길이 등을 판별할 때 유용하게 사용할 수 있다.
- fast runner와 slow runner 간의 step을 2배 차이를 두는 식으로 (ex. fast, slow = 2,1) 지정한 후 fast runner가 리스트의 끝지점에 도착하면 slow는 정확히 리스트의 중간 지점에 도달하게 된다.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head
        # 런너를 이용해 역순 연결 리스트 구성
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
            # rev = 2 -> 1 -> None
            # slow = 2 -> 1 -> None
            # fast = 1 -> 2 -> None
				# 주어진 연결 리스트의 노드 개수가 홀수일 경우 slow 포인터를 한번 더 움직여서 중앙에 위치시킨다.
        if fast:
            slow = slow.next
        
        # 팰린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
            
        return not rev
```

Example 1을 예로 들면 역순 리스트를 구성했을 때 

rev 리스트는 2 -> 1 -> None
slow 포인터의 위치는  2 -> 1 -> None가 된다.

다음 while문 로직을 통해 rev가 None이 될 때까지 rev 값과 slow 값을 비교하여 팰린드롬 여부를 확인한다.

만약, rev 값이 None이 아니면 팰린드롬이 아닌 것이다. 따라서 Example 1의 결과는 True를 반환한다.

Example 2는 역순 리스트가 1 → 2가 되고 slow 포인터는 2 → None이 된다.

그래서 팰린드롬 여부를 확인 할 때 rev 값과 slow 값이 다르기 때문에 반복문을 실행하지 않고, rev가 None이 아니기 때문에 False를 반환하게 된다. 따라서 Example 2는 팰린드롬이 아니다.