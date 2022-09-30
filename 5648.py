# 원자들의 움직임 시뮬레이션
# 1. 원자가 충돌하면 에너지 방출하고 소멸
# 2. 각자는 움직이는 방향을 가진다.
# 3. 이동속도는 일정(1초에 1)
# 4. 최초 위치에서 동시에 이동 시작
# n개 원자 x,y위치, 이동방향, 에너지가 주어질때 방출 에너지 총합
from collections import deque
T = int(input())
for ct in range(1,T+1):
    n = int(input()) # 원자 개수 1~1000
    direction = {0:(0,1),1:(0,-1),2:(-1,0),3:(1,0)} # (0:상 1:하 2:좌 3:우)
    visited = dict()
    visited[0] = []
    # 결과는 result
    result = 0
    # BFS를 통해 한칸씩 이동하자
    q = deque()
    for i in range(n):
        x,y,k,size = map(int, input().split())
        # 시간을 정해서 visited에 시간을 기록하고 만약 같은 시간이 있으면 그것에 해당하는 것을 삭제!해줘야한다.
        t = 0
        q.append((2*x+2000,2*y+2000,k,t,size))# 번호, 좌표, 방향, 시간, 크기
    # 각 원자를 저장하기
    explode = []
    visit = [0]*4001
    # 터진 원자들에 대한 정보를 explode에 넣기
    while q:
        x,y,k,t,size = q.popleft()
        if not visit[t]:
            visited[t+1] = []
        if (x,y,t) in explode: # 이미 터진 원자면 고려 안한다.
            result += size # 대신 터진 정보는 result에 더해준다.
            continue
        dx,dy = direction[k]
        nx, ny = x + dx, y + dy # 한 칸 이동하기
        t+=1
        if nx<0 or ny<0 or nx>=4001 or ny>=4001: # 범위가 벗어나면 고려대상 아니다.
            continue
        elif (nx,ny) in visited[t]: # 이미 누가 방문한 곳이 나랑 같은 타이밍이면
            explode.append((nx,ny,t)) # 터진 곳으로 기록한다.
        else:
            visited[t].append((nx,ny))
        q.append((nx,ny,k,t,size)) # 터진곳의 정보를 result에 넣어 주기 위해 q에 넣는다.
    print(f'#{ct} {result}')
    
