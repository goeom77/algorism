# n개 수중 i번째 수부터 j번째 수까지 합구하기
import sys
n,m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
dp = [0]*(n+1) # n 까지 누적합
max_num = 0
arr = [None]*m
for k in range(m):
    i,j = map(int, sys.stdin.readline().split())
    arr[k] = (i,j)
    if j > max_num:
        max_num = j
for i in range(max_num):
    dp[i+1] = dp[i] + num[i]
for i,j in arr:
    print(dp[j]-dp[i-1])
    