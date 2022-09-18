# 찾았다 악질
# 악질 스트리머 찾기
# 특정 기간 내 시청자 차이합이 2000넘으면 좋지 않다.
# 시청자가 구독한 스트리머 수 n 시청자 변화 추이 m
import sys
n, m = map(int, sys.stdin.readline().split())
# 랄파의 시청자 추이
L = list(map(int, sys.stdin.readline().split()))
result = 0
for i in range(n-1):
    a = list(map(int, sys.stdin.readline().split()))
    cnt = 0
    for j in range(m):
        cnt += abs(L[j] - a[j])
    if cnt > 2000:
        result += 1
# result = 랄파와 사이 안좋은 스트리머
if result >= ((n-1)/2):
    print('YES')
else:
    print('NO')
# 악질이면 yes 아니면 no