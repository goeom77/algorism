#동전
# n 종류 돈전
#필요한 동전 개수 최솟값
n, k = map(int, input().split())
coin = []
for i in range(n):
    coin.append(int(input()))
cnt = 0
for i in range(n-1,-1,-1):
    if k == 0:
        break
    if coin[i] <= k:
        cnt += (k//coin[i])
        k %= coin[i]
        
print(cnt + k)