# 내려가기
# 바로 밑, 바로 옆만 갈수 있다.
# 0~9, n = 1~100000
import sys
input = sys.stdin.readline
n = int(input())
mx_dp = [[0,0,0] for _ in range(2)]
mn_dp = [[0,0,0] for _ in range(2)]

for j in range(n):
    i = j % 2
    graph = list(map(int,input().split()))
    mx_dp[i][0] = max(mx_dp[i-1][0]+graph[0],mx_dp[i-1][1]+graph[0])
    mx_dp[i][1] = max(mx_dp[i-1][0]+graph[1],mx_dp[i-1][1]+graph[1],mx_dp[i-1][2]+graph[1])
    mx_dp[i][2] = max(mx_dp[i-1][1]+graph[2],mx_dp[i-1][2]+graph[2])
    mn_dp[i][0] = min(mn_dp[i-1][0]+graph[0],mn_dp[i-1][1]+graph[0])
    mn_dp[i][1] = min(mn_dp[i-1][0]+graph[1],mn_dp[i-1][1]+graph[1],mn_dp[i-1][2]+graph[1])
    mn_dp[i][2] = min(mn_dp[i-1][1]+graph[2],mn_dp[i-1][2]+graph[2])


print(max(mx_dp[n%2-1]),min(mn_dp[n%2-1]))
