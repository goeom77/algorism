# n*n 공간에 m마리 물고기와 상어 1마리
# 1칸에는 최대 1마리
# 상어는 크기가 2
# 큰물고기가 있는 칸은 갈수 없고, 나머지는 갈수 있다.작은 물고기 먹을수 있음
# 더이상 먹을 물고기가 없으면 엄마상어에게 요청
# 가장 가까운 물고기부터 먹는다
# 같은거리라면 가장 위에 있는 물고기 왼쪽에 잇는 물고기 먹는다.
# 크기와 합이 같은 크기를 먹으면 크기 1증가
# 이동 1당 1초 소모
# n 2~20
n = int(input())
# 9는 아기 상어 위치
# 1,2,3,4,5,6 물고기 크기
sea = [list(map(int,input().split())) for _ in range(n)]
fish = [0]*7
st_p = []
for i in range(n):
    for j in range(n):
        if 0 < sea[j][i] <= 6:
            fish[sea[j][i]] += 1
        if sea[j][i] == 9:
            st_p.append((i,j))
st_p.sort()
for i in range(1,7):
    fish[i] //= i
size = 2
eat = 0
# 먹은것이 크기이면 eat은 reset하고 size는 +1
