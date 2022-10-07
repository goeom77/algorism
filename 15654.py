# n과 m(5)
# 길이가 m인 수열 모두 구하기

def combo(n,m):
    if n==m:
        cnt = []
        for k in range(m):
            cnt.append(chosen[k][1])
        result.append(cnt[:])
        return
    for i in range(len(arr)):
        if arr[i] in chosen:
            continue
        chosen[n] = arr[i]
        combo(n+1,m)

n, m = map(int, input().split())
arr = list(map(int,input().split()))
arr.sort()
arr = list(enumerate(arr))
chosen = [None]*m
result = []
combo(0,m)
for i in range(len(result)):
    tmp = list(set(result[i]))
    print(*tmp)
