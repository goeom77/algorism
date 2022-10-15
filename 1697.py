# 숨바꼭질
# 수빈0~100000 동생 0~100000
# 수빈이는 걷거나 순간이동 가능
# 걷는건 x-1 x+1
# 순간이동 2*x
# 가장 빠르게 찾는 시간 출력
from collections import deque
n,k = map(int, input().split())

dp = [0]*(min(k*2,100001))
q = deque([k])
while q:
    num = q.popleft()
    if num == k:
        continue
    a = num - 1
    b = num + 1
    c = num//2
    if a >= 0 and dp[a] <= dp[num]:
        dp[a] = dp[num] + 1
        q.append(a)
    if b <= 100000 and dp[b] <= dp[num]:
        dp[b] = dp[num] + 1
        q.append(b)
    if not num%2 and dp[c] <= dp[num]:
        dp[c] = dp[num] + 1
        q.append(c)
    
print(dp[k])

