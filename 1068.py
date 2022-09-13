# n이 50보다 작은 노드 주어진다.
# 부모가 없으면 -1 지울노드의 번호를 주면 리프 노드의 개수 출력
from collections import deque
n = int(input())
arr = list(map(int,input().split()))
ch1 = [-1]*(n) # left
ch2 = [-1]*(n) # right

root = -3
for i in range(n):
    # 0으로 가는경우 있는 건지 확인하기 어려우니깐 1부터 n+1까지로 변경
    if arr[i] == -1:
        root = i
    elif ch1[arr[i]]!=-1:
        ch2[arr[i]] = i
    else:
        ch1[arr[i]] = i
        # arr[i] 는 부모노드, i는 자식노드

result = 0
# 제거된 자식들을 제거해야한다.
v = int(input())
stack = [v]
stack = deque(stack)
while stack:
    w = stack.popleft()
    if ch2[w] != -1:
        stack.append(ch2[w])
    if ch1[w] != -1:
        stack.append(ch1[w])
    ch1[w] = ch2[w] = -2
# 부모 노드만 있고 자식노드가 없는 것을 찾아야한다.
for i in range(n):
    # 자식노드중에 하나가 없어진 경우 그것이 리프가 된것도 고려해줘야한다.
    if ch1[i] == -1 and ch2[i] == -1:
        result += 1
    elif ch1[i] == v or ch2[i] == v:
        if ch1[i] == -1 or ch2[i] == -1:
            result += 1
if v == root:
    print(0)
else:
    print(result)