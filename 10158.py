# 개미
# w 가로 h 세로 2~40000
w, h = map(int,input().split())
# 개미는 부딪치면 45도 방향으로 움직인다.
# 1시간에 1칸을 들린다.
# 지금 위치
x, y = map(int,input().split())
t = int(input())
# t < 200000000
# x, y따로 생각해서 0~ w , 0~ h 사이에 움직이는 걸로 판단
rxt = t % (2*w)
ryt = t % (2*h)
if rxt <= w -x:
    x += rxt
elif rxt <= 2*w - x:
    x = 2*w - (rxt + x)
else:
    x = rxt - (2*w - x - 1)
if ryt <= h - y:
    y += ryt
elif ryt <= 2*h - y:
    y = 2*h - (ryt + y)
else:
    y = ryt - (2*h - y - 1)
print(x, y, sep=" ")