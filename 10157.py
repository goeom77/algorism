# 가로 C, 세로 R
c, r = map(int,input().split())
#(1,1) ~ (c,r)까지 좌석 존재 -> (0,0) ~ (c-1, r-1)
# 시계 방향으로 좌석 배정
# k 번째 고객이 앉을 좌석은?
# 고객번호
n = int(input())
arr = [[0]*c for _ in range(r)]
x, y= 0, 0
arr[y][x] = 1
a = False
if n > c*r:
    print(0)
elif n == 1:
    print(1, 1)
else:
    while a == False:
        for dx, dy in [[0,-1],[-1,0],[0,1],[1,0]]: # 상 좌 하 우
            nx = x + dx
            ny = y + dy
            if 0<= nx < c and 0<= ny <r and arr[ny][nx] == 0:
                arr[ny][nx] = arr[y][x] + 1
                x = nx
                y = ny
                if arr[y][x] == n:
                    print(x + 1, y + 1)
                    a = True
                    break
                while True:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < c and 0 <= ny < r and arr[ny][nx] == 0:
                        arr[ny][nx] = arr[y][x] + 1
                        x = nx
                        y = ny
                        if arr[y][x] == n:
                            print(x+1, y+1)
                            a = True
                            break
                    else:
                        break

