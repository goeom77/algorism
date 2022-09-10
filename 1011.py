 # fly me th the alpha centaurti
 # 공간이동 장치
 # k광년 이동하였을 때 k-1,k,k+1광년 이동 가능
 # 음수 불가
 # 최소 작동횟수 시작은 0
 # 0<=x<y<2**31
 # test case
T = int(input())
for t in range(T):
 # 도착은 1광년으로
 # x -> y로
    x, y = map(int,input().split())
    l = y - x
    arr = []
    tmp = 1
    # 숫자를 2개씩 넣었을 때 그 수보다 크면 추가
    while l > 0:
        if l -tmp >0:
            l -= tmp
            arr.append(tmp)
        else:
            break
        if l - tmp >0:
            l -= tmp
            arr.append(tmp)
        else:
            break
        tmp += 1
    print(len(arr)+1)
