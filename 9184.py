# 하나라도 0보다 작거나 같으면 1
# 하나라도 20보다 크면 w(20,20,20)반환
# a<b<c이면 w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c) 반환
# 나머지는 w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1) 반환
dp = [[[0]*20 for _ in range(20)] for __ in range(20)]
while True:
    a,b,c = map(int, input().split())
    if a == -1 and b == -1 and c == -1: # 종료조건
        break
    if a<= 0 or b<= 0 or c<= 0:
        print(f'w({a}, {b}, {c}) = 1')
        continue
    if dp[c][b][a]:
        print(f'w({a}, {b}, {c}) = {dp[c][b][a]}')
        continue
    else:
        
