n,k = map(int, input().split())
coin = []
for _ in range(n):
    a = int(input())
    if a<= k:
        coin.append(a)
coin.sort()
dp = [0]*(k+1)
for j in range(len(coin)):
    dp[coin[j]] += 1
    for i in range(coin[j],k+1):
        dp[i] += dp[i-coin[j]]
print(dp)
        