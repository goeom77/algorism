# n = 정점의 개수 m = 간선의 개수  v 탐색 시작 위치
# 1. DFS 2. BFS
from collections import defaultdict, deque
n , m, v = map(int,input().split())
arr = defaultdict(list)
for i in range(m):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
stk = []
stk = deque()
q = []
q = deque()
dfs_vigited = [0] * (n+1)
bfs_vigited = [0] * (n+1)
dfs_vigited[v] = 1
bfs_vigited[v] = 1
dfs_v = v
stk.append(dfs_v)
bfs_v = v
# DFS
def BFS(v):
    while stk:
        v = stk.popleft()
        for w in arr[dfs_v]:
            if dfs_vigited[w] == 0:
                stk.append(w)
                dfs_vigited[w] = 1
                break


