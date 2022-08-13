T = int(input())
arr = []
for t in range(T):
    a,b = map(int,input().split())
    arr.append([b,a])
arr.sort()
for i in range(len(arr)):
    for j in range(1,-1,-1):
        print(arr[i][j],end=" ")
    print()