# 연구소
# 바이러스 막기위한 벽
# 3~8 n*m 연구소
# 먼저 탐색을 해서 몇개로 막을수 있는지 확인하기
# 두번째로 몇개 손해보고 막을수 있는 지 확인하기
n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
stp = []
for j in range(n):
    for i in range(m):
        if arr[j][i] == 2:
            stp.append((j,i))
# bfs로 가되 그 지점을 4방향 비교했을 때 2곳 다 3개로 막을수 있는 장소이면 스탑

