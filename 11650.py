import sys

T = int(input())
arr = []
for t in range(T):
    a,b = map(int,sys.stdin.readline().split())
    arr.append((a,b))
arr.sort()
for i in range(len(arr)):
    for j in range(2):
        print(arr[i][j],end=" ")
    print()