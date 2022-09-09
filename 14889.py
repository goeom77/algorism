# 사람 수 n = even
# 1~n까지 배정해서 팀의 능력치를 더한게 s12, s21 된게 그 팀의 능력치
# 게임의 재미를 위해 능력치 차이를 최소로 하려고 한다.
n = int(input())
ability = list(list(map(int,input().split())) for _ in range(n))
# 아래 삼각형에 위 삼각형의 값의 대칭값을 더해준다.
for j in range(n):
    for i in range(j+1,n):
        ability[i][j] += ability[j][i]
# 1,2,3 팀이면 4,5,6 팀
# j > i인 조건에서만 더할것
# 팀을 먼저 나누자
def team(n):
    