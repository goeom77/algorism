# 겹치는 부분이 직사각형이면 a 선분이면 b 점이면 c 없으면 d
# 사각형은 좌하, 우상으로 표시
# 예시는 4가지
for i in range(4):
    a, b, c, d, e, f, g, h = map(int,input().split())
    # x = a c ,e g
    # y = b d ,f h
    # 선이 겹치면 b
    if (c == e and d == f) or (g == a and h == b):
        result = 'c'
    elif (a == g and f == d) or (c == e and b == h):
        result = 'c'
    elif (d == f and e < c and a < g) or (c == e and f < d and b < h) or (g == a and b < h and f < d) or (h == b and a < g and e < c):
        result = 'b'
    # 안겹칠 때
    elif d < f or c < e or g < a or h < b:
        result = 'd'
    else:
        result = 'a'
    print(result)