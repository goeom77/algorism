import sys

T = int(input())
arr = []
for t in range(T):
    a = sys.stdin.readline()
    arr.append(a)
arr.sort()
for i in arr:
    print(i)