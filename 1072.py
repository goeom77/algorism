# 게임

# 앞으로의 게임에서 지지않는다.
# 게임횟수 : x(<=1000000000)
# 이긴횟수 : y(z%) z에서 소숫점은 버린다.
# z가 언제 변하는지 구하여라
# z가 변하지 않으면 -1출력

x, y = map(int,input().split())
if (y*100)//x >= 99:
    print(-1)
else:
    z = (y*100//x)
    result = z
    cnt = 0
    if x >= 100000000:
        while True:
            cnt += 1000000
            z = (y+cnt)*100//(x+cnt)
            if result == z:
                pass
            else:
                cnt -= 1000000
                break
    if x >= 1000000:
        while True:
            cnt += 10000
            z = (y+cnt)*100//(x+cnt)
            if result == z:
                pass
            else:
                cnt -= 10000
                break
    if x >= 1000:
        while True:
            cnt += 100
            z = (y+cnt)*100//(x+cnt)
            if result == z:
                pass
            else:
                cnt -= 100
                break
    while True:
        cnt += 1
        z = (y+cnt)*100//(x+cnt)
        if result != z:
            print(cnt)
            break

        

