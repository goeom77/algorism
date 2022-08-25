T = int(input())

for t in range(1,T+1):
    m,n,tc = map(int,input().split())
    ground = [[0]*m for _ in range(n)]
    dx = [-1,1,0,0] # 좌 우 상 하
    dy = [0,0,-1,1]
    worms = 0
    visited = []
    def search(a,b):
        global visited
        cnt = 0
        for k in range(4):
            if 0 <= j + dy[k] < n and 0 <= i + dx[k] < m and (i+dx[k], j+dy[k]) not in visited:
                if ground[j + dy[k]][i + dx[k]] == 1:
                    visited.append((i+dx[k],j+dy[k]))
                    search(i+dx[k], j+dy[k])
    for c in range(tc):
        a,b = map(int,input().split())
        ground[b][a] = 1
    for i in range(m):
        for j in range(n):
            if ground[j][i] == 1 and (i,j) not in visited:
                worms += 1
                search(i,j)
    print(worms)

