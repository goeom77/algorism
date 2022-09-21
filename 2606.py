# 바이러스

# 컴퓨터 수 1~100 번호 1~100까지 호칭
com = int(input())
T = int(input())
arr = dict()
for i in range(1,com+1):
    arr[i] = []
for t in range(T):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
visited = [0]*(1+com)
q = [1]
while q:
    st = q.pop() #  시작
    for i in arr[st]:
        if visited[i] == 0:
            visited[i] = 1
            q.append(i)
print(sum(visited)-1)



    
