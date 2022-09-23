# n*n 홈방법 서비스
# 마름모 형태에서만 제공된다.
# 운영비용이 필요
# k 크기가 커질수록 비용 상승
# 비용 : k*k + (k-1)*(k-1)
# k>=1
# 홈방법서비스를 가장 많은 집들에 제공하는 서비스 영역을 찾고, 이때 제공 받는 집들의 수 출력
# 수익 = m*집개수
# 도시 크기 n 5~20
# map에서 집은 1 나머지는 0
# 최소 하나의 집은 존재
from collections import deque
import math
def search_size(i,j):
    global result # 집의 최소 개수는 1이니깐 1을 base로 두기
    global n
    h = 0
    q = deque([(i,j)])
    visited[j][i] = 1 # k가 1인경우
    if arr[j][i] == 1:
        h += 1
    cnt = 3  #k를 2까지 확인하고 3인 된 경우 h측정하면 k가 2까지 확인
    while q:
        x,y = q.popleft() # BFS풀기
        for dx,dy in [[0,1],[0,-1],[1,0],[-1,0]]:  # 4방향 모두 확인
            nx = x + dx
            ny = y + dy
            if nx<0 or ny<0 or nx>= n or ny >= n or visited[ny][nx]:
                continue                        # 방문한곳, 범위 밖은 계산 x
            q.append((nx,ny))
            visited[ny][nx] = visited[y][x] + 1
            if visited[ny][nx] == cnt:
                if home[cnt] <= h and result < h: # 집의 최소개수를 만족하면서, 결과값보다 큰경우
                    result = h
                cnt += 1
            if arr[ny][nx] == 1:
                h += 1




T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # 집은 항상 1개 있고 수익은 1개일때 1이므로 기본 값은 1이다.
    home = []
    # 결과값의 최소 개수는 1이니깐 지정
    result = 1
    # k가 1일때 home[1]에 필요한 집의 최소개수가 들어간다.
    for k in range(2*n):
        l = math.ceil((k*k +(k-1)*(k-1))/m)
        home.append(l)
    print(home)
    # cost = h(집개수)*m - (k*k +(k-1)*(k-1)) > 0 할수 있다.
    # k를 지정할 때 최대 h의 개수를 세야한다.k의 최대 범위는 2 ~ 20
    # 방문한 곳인지 판단하는 것
    ck = True
    for j in range(n):
        for i in range(n):
            if result == n**2:
                break
            visited = [[0]*n for _ in range(n)]
            search_size(i,j)

    print(f'#{t} {result}')