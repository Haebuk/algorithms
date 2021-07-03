t = [3,5,1,1,2,4,2]
p = [10,20,10,20,15,40,200]
n = len(t)
max_value = 0
dp = [0] * (n+1)
for i in range(n-1, -1, -1):
    time = t[i] + i
    if time <= n:
        dp[i] = max(max_value, p[i] + dp[time])
        max_value = dp[i]
    else:
        dp[i] = max_value
    print(max_value, dp) 
print(max_value)
