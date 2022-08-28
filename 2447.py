# 땅에 자라는 참외 개수
from collections import deque
t = int(input())
# v = 동 1 서 2 남 3 북 4
a = []
b = []
# a는 방향의 리스트 b는 거리의 리스트
for i in range(6):
    v, r = map(int, input().split())
    a.append(v)
    b.append(r)
# fa가 1개인 것들 -> 그것들의 index를 삭제해서 중간값들의 크기를 빼주면된다.
fa = []
b = deque(b)
for i in range(1, 5):
    if a.count(i) == 1:
        fa.append(i)
fb = a.index(fa[0])
fc = a.index(fa[1])
# 회전 필요량
if abs(fb-fc) == 1:
    lo = -min(fb,fc)
else:
    lo = 1
# 회전이 1차이날때는 작은값만큼 돌리고 처음과 끝에 있을 때는 1만큼 돌려서 제일 앞으로 위치시킨다.
b.rotate(lo)
m = b.popleft()
n = b.popleft()
result = abs((m * n) - (b[1] * b[2]))

print(result * t)