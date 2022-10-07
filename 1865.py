# 웜홀
# n개 지점 , m개 도로와 w개 웜홀(도로는 방향 x 웜홀은 방향 o)
# 웜홀은 시간이 뒤로 간다,.
# 시간이 이동후 더 뒤인 경우를 구하는 프로그램 작성
import sys
input = sys.stdin.readline
T = int(input())
for t in range(1, T+1):
    N,M,W = map(int, input().split()) # n 노드 , m 도로 , w 웜홀
    graph = [[] for _ in range(N+1)]
    for i in range(M):
        s,e,t = map(int,input().split())
        graph[s].append(e,t)
        graph[e].append(s,t)
    for i in range(W):
        s,e,t = map(int,input().split())
        graph[s].append(e,-t)
    # 자기자신에게 돌아올때 시간이 (-)가 되는것이 있는가 있으면 YES 없으면 NO
