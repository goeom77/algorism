# 30번
# M(a,b) 를 완전이진트리에서 공통의 루트를 구하시오.
T = int(input())
for t in range(T):
    a, b= map(int, input().split())
    if a> b:
        a, b = b, a
    a_layer = 0
    b_layer = 0
    # 0~10층까지
    l = [1,2,4,8,16,32,64,128,256,512,1024]
    for i in range(1,11):
        if l[i-1] <= a < l[i]:
            a_layer = i
        if l[i-1] <= b < l[i]:
            b_layer = i
    gap = b_layer - a_layer
    for i in range(gap):
        b //= 2
    while a != b:
        a //= 2
        b //= 2

    print(a*10)
