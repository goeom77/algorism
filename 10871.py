n, a = map(int,input().split())
arr = list(map(int,input().split()))
brr = []
for i in range(n):
    if arr[i]<a:
        brr.append(arr[i])
print(*brr,sep=' ')
        