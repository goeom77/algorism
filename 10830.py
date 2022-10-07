n, b = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
result = arr[:]
arr = zip(*arr)
for _ in range(b):
    cnt = result[:]
    for j in range(n):
        for i in range(n):
            tmp = 0
            for k in range(n):
                tmp += cnt[j][i]*

