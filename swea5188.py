# 최소합
from collections import deque
T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # visited에 최소합 기록
    visited = [[0]*n for _ in range(n)]
    # 우, 하 로만 움직이는 모든 케이스
    q = deque()
    q.append((0,0))
    # 큐를 통해 확인한다.bfs
    visited[0][0] = arr[0][0]
    while q:
        x,y = q.popleft()
        for dx, dy in [[1,0],[0,1]]:
            nx = x+dx
            ny = y+dy
            if nx>=n or ny>=n:
                pass
            else:
                temp =  arr[ny][nx] + visited[y][x]
                if visited[ny][nx] == 0:
                    visited[ny][nx] = temp
                    q.append((nx,ny))
                else:
                    if visited[ny][nx] > temp:
                        visited[ny][nx] = temp
    print(f'#{t} {visited[n-1][n-1]}')

