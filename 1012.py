T = int(input())

for t in range(1,T+1):
    m,n,tc = map(int(input()))
    ground = [[0]*m for _ in range(n)]
    for c in range(tc):
        a,b = map(int(input()))
        ground[b][a] = 1
    