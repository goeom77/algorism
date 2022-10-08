import heapq
n, d = map(int, input().split())
# 최대가 10000개이기 때문에 다 익스트라로 하기에는 조금 많음
# 지름길 개수, 총거리
INF = int(1e8)
graph = [[] for _ in range(d+1)]
distance = [INF]*(d+1)
for i in range(d):
    graph[i].append((i+1,1))
for i in range(n):
    a, b, c = map(int, input().split())
    # 출발 도착 길이
    if b-a < c:
        continue
    elif b > d:
        continue
    else:
        graph[a].append((b,c))
        # 지름길 a 에서 b로 가는데 c가 걸린다.


def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 거리가 크면
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0])) # DFS

dijkstra(0)
print(distance[d])