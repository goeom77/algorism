# 뱀은 사과 먹으면 길이 1 길어진다.
# 머리가 몸에 다이면 끝
# 사과먹으면 사과 자리에 머리가 생긴다.
# 사과 없으면 사과 자리에 머리 넣고 꼬리 1짧아진다.
# 보드 크기 n 
n = int(input())
board = [[0]*n for _ in range(n)]
# 사과 개수 k
k = int(input())
for i in range(k):
    y, x= map(int,input().split())
    board[y-1][x-1] = 1
# 머리 변환 횟수L
L = int(input())
turn = []
for l in range(L):
    t, info = input().split()
    turn.append((int(t),info))
    # info가 l이면 왼쪽 90도 D이면 오른쪽 90도
# 게임이 몇초에 끝날지 출력
# 시간은 t
t = 0
# start point 는 좌상 길이는 1 오른쪽으로 향한다
t = [[1,0],[0,1],[-1,0],[0,-1]]# 우 하 좌 상
life = True
head = (0,0)
tail = (0,0)
turn = 0
while life:
    x, y= head
    mx,my = tail
    dx, dy = t[turn]
    nx = x + dx
    ny = y + dy
    
    if 0<= nx < n and 0<= ny < n:
        if board[ny][nx] == 1:
            tail = (mx,my)
            head = (nx,ny)
        
    