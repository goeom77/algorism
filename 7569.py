# 토마토
# 가로 m 세로 n 높이 h
# -1은 안들은 칸
# 밑에서 부터 위로 
from collections import deque
m,n,h = map(int,input().split())
arr = []
for i in range(h):
    arr.append([list(map(int,input().split())) for _ in range(n)])
dx = [0,0,-1,1,0,0]
dy = [1,-1,0,0,0,0]
dk = [0,0,0,0,1,-1]
q = deque()
# q를 통해 모든 곳의 근처지역을 날짜 +1로 만든다.
for k in range(h):
    for y in range(n):
        for x in range(m):
            if arr[k][y][x] == 1:
                q.append((k,y,x))
while q:
    k, y, x = q.popleft()
    for p in range(6):
        nk = k + dk[p]
        ny = y + dy[p]
        nx = x + dx[p]
        if 0<= nk < h and 0<= ny < n and 0<= nx <m:
            if arr[nk][ny][nx] == 0:
                q.append((nk,ny,nx))
                arr[nk][ny][nx] = arr[k][y][x] + 1
result = 0
no_way = False
for k in range(h):
    for j in range(n):
        for i in range(m):
            if arr[k][j][i] > result:
                result = arr[k][j][i]
            if arr[k][j][i] == 0:
                no_way = True
if no_way:
    print('-1')
else:
    print(result-1)