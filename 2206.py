# 벽을 한개 부숴도 된다.
# 못가면 -1 출력
# 벽을 부술 때 1. 어쩔수 없이 부숴야 하는 경우 2. 거리를 줄이기 위해 부수는 경우
# 길은 0 벽은 1
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
stack = [(0,0)]
visited[0][0] = 1
# 벽 부수는 용 hammer
hammer = True
while stack:
    cnt = 0
    x, y = stack.pop()
    # visited에 걸리는 거리를 출력하자
    for i, j in [[0,1],[0,-1],[1,0],[-1,0]]:
        nx = x + i
        ny = y + j
        if 0<= nx <m and 0<= ny < n :
            if visited[ny][nx] == 0 and arr[ny][nx] == 0:
                stack.append((nx,ny))
                visited[ny][nx] = visited[y][x]+1
            else:
                cnt +=1
        else:
            cnt += 1
    if cnt == 4 and hammer:
        for i, j in [[0,2],[0,-2],[2,0],[-2,0]]:      
            nx = x + i
            ny = y + j
            if 0<= nx <m and 0<= ny < n and visited[ny][nx] == 0 and arr[ny][nx] == 0:
                stack.append((nx,ny))
                visited[ny][nx] = visited[y][x] + 2
                hammer = False
result = visited[n-1][m-1]
if result == 0:
    print('-1')
else:
    print(result)

