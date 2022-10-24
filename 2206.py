# 벽을 한개 부숴도 된다.
# 못가면 -1 출력
# 벽을 부술 때 1. 어쩔수 없이 부숴야 하는 경우 2. 거리를 줄이기 위해 부수는 경우
# 길은 0 벽은 1
import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
arr = list(input() for _ in range(n))
result = []
# 다음 시도에 해볼것
# 가는길에 나오는 첫 걸림돌을 부수고, 그 부슨 것을 리스트에 넣기
# 3면 이상이 1로 막힌 경우는 빼기

visited = [[0]*m for _ in range(n)]
q = deque([(0,0,1)])
visited[0][0] = 1
while q:
    x, y, hammer = q.popleft()
    # visited에 걸리는 거리를 출력하자
    for i, j in [[0,1],[0,-1],[1,0],[-1,0]]:
        nx = x + i
        ny = y + j
        if 0<= nx <m and 0<= ny < n :
            if hammer and visited[ny][nx] == 0 and arr[ny][nx] == '1':
                q.append((nx,ny,0))
                visited[ny][nx] = visited[y][x]+1    
            elif visited[ny][nx] == 0 and arr[ny][nx] == '0':
                q.append((nx,ny,hammer))
                visited[ny][nx] = visited[y][x]+1
            elif visited[ny][nx] < visited[y][x] and arr[ny][nx] == '0':
                q.append((nx,ny,hammer))
                visited[ny][nx] = visited[y][x]+1                
result = visited[n-1][m-1]
if result == 0:
    print('-1')
else:
    print(result)