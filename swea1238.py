# 비상연락망
# r은 연락 시작 당번
# 마지막에 동시에 연락 받은 사람중에서 숫자가 가장 큰 사람을 반환할것
# 1~100 번호도 100까지
# 한번 통화시 다자에게 한번에 통화
from collections import deque
for t in range(1,11):
    n, start = map(int,input().split())
    arr = list(map(int, input().split()))
    data = [[0] for _ in range(101)]
    for i in range(int(n//2)):
        a,b = arr[2*i],arr[2*i+1]
        if data[a][0]:
            data[a].append(b)
        else:
            data[a][0] = b
    visited = [0]*101
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        a = q.popleft()
        if data[a][0] == 0:
            pass
        else:
            for i in data[a]:
                if visited[i]:
                    pass
                else:
                    visited[i] = visited[a] + 1
                    q.append(i)
    h = max(visited)
    for i in range(100,-1,-1):
        if visited[i] == h:
            result = i
            break
    print(f'#{t} {result}')
