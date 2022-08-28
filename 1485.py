# 네점이 주어졌을 때 네점으로 정사각형 가능한가?
# -100000 ~ 100000
# 만들수 있으면 1, 없으면 0
# 4개의 점만 주어진다.
T = int(input())
for t in range(T):
    arr = []
    for i in range(4):
        x, y = map(int,input().split())
        arr.append([x,y])
    arr.sort()
    a = (abs(arr[0][0] - arr[1][0])**2 + abs(arr[0][1] - arr[1][1])**2)
    b = (abs(arr[1][0] - arr[3][0])**2 + abs(arr[1][1] - arr[3][1])**2)
    c = (abs(arr[3][0] - arr[2][0])**2 + abs(arr[3][1] - arr[2][1])**2)
    d = (abs(arr[2][0] - arr[0][0])**2 + abs(arr[2][1] - arr[0][1])**2)
    e = (abs(arr[0][0] - arr[3][0])**2 + abs(arr[0][1] - arr[3][1])**2)
    f = (abs(arr[1][0] - arr[2][0])**2 + abs(arr[1][1] - arr[2][1])**2)
    if a == b == c == d and e == f:
        print(1)
    else:
        print(0)
