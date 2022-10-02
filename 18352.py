# 특정 거리의 도시 찾기
# n번 까지 도시, m개의 도로 존재
# x에서 출발해 최단거리가 k인 도시 번호 출력
import sys

n,m,k,x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
INF = int(1e8)
distance = [INF]*(n+1)

for i in range(m):
    s, a = map(int, sys.stdin.readline().split())
    graph[s].append(a) # s -> a 로 가는 비용은 1

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]: # 정보가 들어간 곳 중 가장 낮은 곳의 인덱스 출력
            min_value = distance[i]
            index = i
    return index

def dijkstra(x):
    distance[x] = 0  # 출발점 x = 0
    visited[x] = True # 방문처리
    for j in graph[x]: # 출발점에서 갈수 있는 곳 거리정보 넣기
        distance[j] = 1
    # 거리에 대한 정보 넣기
    for i in range(n-1): # 출발점 제외한 거리 찾기
        now = get_smallest_node()
        # print(now)
        visited[now] = True # 그리디 방법을 통해 거리가 결정되면 고정
        for j in graph[now]: # 고정된 노드로 부터 또 출발
            cost = distance[now] + 1
            if cost < distance[j]: # 여러가지 방법 중 가장 최소의 방법으로 코스트 부여
                distance[j] = cost
dijkstra(x)
result = []
# print(visited)
# print(distance)
for i in range(len(distance)):
    if distance[i] == k:
        result.append(i)
if not len(result):
    print('-1')
else:
    for i in result:
        print(i)
        
