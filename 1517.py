import sys
from tkinter import N

num = int(input())
arr = sys.stdin.readline().rstrip().split()
n = len(arr)
search = 0
stack = 0
for i in range(n):
    plus = arr[i] -i -1
    if plus < 0 :
        plus = 0
    if stack != 0:
        search += plus
print(search)


