import sys
n = int(input())

arr = list(map(int, sys.stdin.readline().split()))
dp = [0]*n
dp[0] = 0 # 첫번째는 비교대상이 없으므로
for j in range(1,n):
    for i in range(j):
        if arr[i] <arr[j]:
            dp[i] = max(dp[j],dp[i]+1)
print(max(dp))
