# 용액
INF = int(2e9)
n = int(input())
arr = list(map(int, input().split()))
total = INF
result = 0
ck = 1
for j in range(n):
    for i in range(n-1,j,-1):
        if abs(arr[j]+arr[i]) < total:
            total = abs(arr[j]+arr[i])
            result = (arr[j],arr[i])
        else:
            break
    if arr[j]>0:
        ck = 0