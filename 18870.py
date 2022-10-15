import sys

n = int(input())
num = list(map(int, sys.stdin.readline().split()))
sorted_num = list(set(num))
sorted_num.sort()
rank = [0 for _ in range(n)]
for i in range(n):
    for j in range(len(sorted_num)):
        if num[i] == sorted_num[j]:
            rank[i] = j
            break

print(*rank)