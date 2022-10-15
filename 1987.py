# 알파벳
# r*c 보드(세로 가로)
# 0,0 = 1행 1열 은 말이 있다.
# 같은 알파벳 지나갈수 없다.
# 최대 몇칸을 지날수 있는지를 구하는 프로그램을 작성하시오.

r,c = map(int,input().split())
board = [list(input()) for _ in range(r)]
def BFS(a):
    visited = []
    
stack = []
stp = [(0,0,1,[])]
result = 0
ban = []
# 몇번째로 갔는지 tmp를 각 인덱스에 마지막에 부여하자
tmp = 0
# dfs로 깊게 파는 방법을 강구해야할듯
while stp:
    # 4방향 모두 있는지 체크
    ab = 0
    x, y, c,tmp= stp.pop()
    c += 1
    visited = tmp.append(board[y][x])
    for i, j in [[0,1],[0,-1],[1,0],[-1,0]]: # 우 좌 하 상
        nx = x + i
        ny = y + j
        try:
            if 0 <= nx < c and 0<= ny < r and board[ny][nx] not in visited and (nx,ny,c) not in ban:
                stp.append([nx,ny,c,visited])
            else:
                ab += 1
        except:
            ab += 1
    if ab == 4:
        c -= 1
        if result < c:
            result = c
        # ban을 c가 똑같은 인덱스만 못가게 해야하므로
        ban.append(x,y,c)
        visited.pop()
print(result)
        
