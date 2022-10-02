# 치즈
from collections import deque
# 4변중 2변이 실내와 닿이면 녹는다. 몇시간 뒤에 다 녹는가?
n,m = map(int,input().split())
# 세로, 가로
arr = [list(map(int,input().split())) for _ in range(n)]
cnt = 0
melt = []
while True:
    cnt += 1
    q = deque([(0,0)])
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    ck = 0
    # bfs로 닿은 회수를 카운트 해서 2회보다 큰 곳은 삭제하고 다시 카운트
    while melt:
        j,i = melt.pop()
        arr[j][i] = 0
    while q:
        j,i = q.popleft()
        for dj, di in [[0,1],[0,-1],[1,0],[-1,0]]:
            nj = dj + j
            ni = di + i
            if nj<0 or nj>=n or ni<0 or ni>=m or visited[nj][ni]:
                continue
            elif arr[nj][ni] == 1:
                visited[nj][ni] += 1
                if visited[nj][ni] >= 2:
                    print(nj,ni)
                continue
            visited[nj][ni] = 1
            ck += 1
            q.append((nj,ni))
    if ck == n*m:
        break
print(cnt)
    