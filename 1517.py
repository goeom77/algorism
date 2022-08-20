import sys
from tkinter import N

num = int(input())
arr = sys.stdin.readline().rstrip().split()
n = len(arr)
search = 0
for i in range(n):
    search += (int(arr[i])-i-1)
    print(search)
print(search)


