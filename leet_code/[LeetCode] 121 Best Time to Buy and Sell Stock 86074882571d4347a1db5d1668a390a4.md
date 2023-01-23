
생성일: 2022년 12월 14일 오전 2:42
태그: Easy, 구현, LeetCode, Python

[Best Time to Buy and Sell Stock - LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

### 난이도: Easy

You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

You want to maximize your profit by choosing a **single day** to buy one stock and choosing a **different day in the future** to sell that stock.

Return *the maximum profit you can achieve from this transaction*. If you cannot achieve any profit, return `0`.

**Example 1:**

```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

```

**Example 2:**

```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

```

**Constraints:**

- `1 <= prices.length <= 105`
- `0 <= prices[i] <= 104`

### 1. 나의 풀이(오답)

- 리스트에서 가장 작은 값과 그 값의 인덱스를 변수에 저장
- 가장 작은 값의 인덱스부터 마지막 인덱스까지의 리스트에서 가장 큰 값을 변수에 저장
- 두 값의 차를 return한다.

Example 1, 2는 통과하였으나, 본 테스트에서는 오답을 출력해 통과하지 못하였다. 이유는 배열의 가장 작은 값이 마지막 인덱스에 위치해 있는 경우에 0을 출력해버리는 것이다.

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price_min = min(prices)
        i = prices.index(price_min)

        price_max = max(prices[i:])
        return price_max - price_min
```

### 2. 저점과 현재 값과의 차이 계산

- 가장 작은 값을 저장할 변수 min_price를 sys.maxsize로 선언한다.
- 배열을 순환하며 min_price를 계속 갱신하면서 현재 값과 min_price의 값의 차이를 계산한다.
- 순환이 끝나면 가장 큰 차이를 반환한다.

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize

        # 최솟값과 최댓값을 계속 갱신
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
            
        return profit
```

실행시간은 2813ms로 꽤나 오래 걸렸다. 다른 사람들의 풀이를 보면 이유는 min() 함수와 max() 함수를 사용해서 그런 것 같다. 자세한 이유는 찾아봐야겠다.

### 다른 사람의 풀이

```python
# 실행시간 778ms
f = open("user.out", 'w')
for line in stdin:
    ans, mn = 0, inf
    for v in map(int, line.rstrip()[1:-1].split(',')):
        if v < mn: mn = v
        if v - mn > ans: ans = v - mn
    print(ans, file=f)
exit(0)
```