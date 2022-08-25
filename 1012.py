from collections import deque

T = int(input())
# m*n 땅에서 배추를 재배한다. 배추 흰지렁이는 배추를 보호한다. 보호하기 위한 배추 흰지렁이는 몇마리인가?
# 배추 흰지렁이는 상하좌우 움직일수 있다.

for t in range(1,T+1):
    m,n,tc = map(int,input().split())
    ground = [[0]*m for _ in range(n)]
    worms = 0
    vigited = [[0]*m for _ in range(n)]
    # worms는 지렁이 개수 지렁이를 visited의 끝까지 stack을 돌리자
    # ground에 지렁이를 한개 넣고 갈수 있는데를 visited에 기록하자
    for c in range(tc):
        a,b = map(int,input().split())
        ground[b][a] = 1
    stk = []
    stk = deque()
    for i in range(m):
        for j in range(n):
            if ground[j][i] == 1 and vigited[j][i] == 0:
                stk.append((i, j))
                vigited[j][i] = 1
                worms += 1
                while stk:
                    x, y = stk.popleft()
                    for dx,dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                        nx ,ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and vigited[ny][nx] == 0 and ground[ny][nx] == 1:
                            stk.append((nx,ny))
                            vigited[ny][nx] = 1

    print(worms)

