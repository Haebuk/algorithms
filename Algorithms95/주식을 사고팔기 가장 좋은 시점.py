# 주식을 사고팔기 가장 좋은 시점
# 한 번의 거래로 낼 수 있는 최대 이익 산출
# 풀이 1. 브루트 포스 계산
def maxProfit(prices):
  max_price = 0

  for i, price in enumerate(prices):
    for j in range(i, len(prices)):
      max_price = max(prices[j] - price, max_price)

  return max_price



# 풀이 2. 저점과 현재 값과의 차이 계산
import sys
def maxProfit(prices):
  # 최댓값을 나타내는 profit은 0보다는 항상 크기 때문에 0으로 설정
  profit = 0
  # 최솟값이 되어야 할 min_price의 초깃값을 가장 큰 값으로 정하여 바로 교체할 수 있게 준비
  min_price = sys.maxsize

  # 최솟값과 최댓값을 계속 갱신
  for price in prices:
    min_price = min(min_price, price)
    profit = max(profit, price - min_price)

  return profit

prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))