# 최단경로
# 정점의 개수, 간선의 개수
from collections import defaultdict
v,e = map(int, input().split())
# 시작 정점
k = int(input())
graph = defaultdict(int)
for i in range(e):
    