# n*n 대나무숲
# 다먹으면 상하좌우 이동
# 옮긴 지역이 그 전 지역보다 대나무가 많아야한다.
import sys
n = int(input())

def DFS():
    cnt = 1
    while q:
        i,j = q.pop()
        for di, dj in [[1,0],[-1,0],[0,1],[0,-1]]:
            ni = i + di
            nj = j + dj
            if ni < 0 or nj < 0 or ni >= n or nj >= n or arr[j][i] <= arr[nj][ni] or visited[nj][ni] > visited[j][i] + 1:
                continue
            visited[nj][ni] = visited[j][i] + 1
            if visited[nj][ni] > cnt:
                cnt = visited[nj][ni]
            q.append((ni,nj))
    return cnt

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = 0
visited = [[0]*n for _ in range(n)]
for j in range(n):
    for i in range(n):
        if not visited[j][i]:
            q = [(i,j)]
            visited[j][i] = 1
            cnt = DFS()
            if cnt > result:
                result = cnt
print(result)
