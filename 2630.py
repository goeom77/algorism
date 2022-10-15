# 색종이 만들기
n = int(input())
c_paper = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
for j in range(n):
    for i in range(n):
        if not visited[j][i]:
            cnt = 1
            