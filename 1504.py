# 특정한 최단 경로
# 방향성 없는 그래프 1->N번 정점 최단 거리 이동 + 특정 두 정점 반드시 통과
import heapq
n, e = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a].append(b,c)
    graph[b].append(a,c)
# c 1~1000
INF = int(1e8)
distance = [INF]*(1+n)
p = list(map(int, input().split()))
# p 들려야하는 정점 2곳

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))