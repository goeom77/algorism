# 색종이 장수n
n = int(input())
# 최대 가로 1001칸 세로 1001칸
arr = [[0]*1001 for _ in range(1001)]
# 색종이 놓인 상태 좌하, 너비, 높이
for t in range(1,n+1):
    x, y, w, h = map(int,input().split())
    for i in range(w):
        for j in range(h):
            arr[y+j][x+i] = t
result = 0
print(arr)
for tmp
print(result)