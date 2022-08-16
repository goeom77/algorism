from collections import deque
T = int(input())
arr = []
for t in range(1,T+1):
    arr.append(t)
q = deque(arr)
while len(q) != 1:
    q.popleft()
    q.rotate(-1)
print(q[0])