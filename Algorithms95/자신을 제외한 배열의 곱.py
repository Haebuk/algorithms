# 자신을 제외한 배열의 곱
# 배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력
# 나눗셈 금지 O(n)로 풀이

# 풀이 1. 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
def productExceptSelf(nums):
  out = []
  p = 1
  # 왼쪽 곱셈
  for i in range(0, len(nums)):
    out.append(p)
    print(p)
    p = p * nums[i]
    
  p = 1
  # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
  for i in range(len(nums) - 1, 0 - 1, -1):
    out[i] = out[i] * p
    p = p * nums[i]
    print(p)
  return out

nums = [1, 2, 3, 4]
print(productExceptSelf(nums))