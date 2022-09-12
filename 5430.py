# AC
# R 뒤집기: 순서를 뒤집는다. D 버리기 : 첫번째 숫자를 버린다.
# 배열이 비어있을 때 D를 하면 error
# case
T = int(input())
for t in range(1,T+1):
    # 함수 1~100000
    f = list(input().strip())
    n = int(input())
    arr = []
    top = 0
    r_arr = input()[1:-1].split(',')
    for i in r_arr:
        if i.isdigit():
            arr.append(int(i))
    bottom = n
    turn = 't'
    end = False
    for i in f:
        if i == 'R':
            if turn == 'b':
                turn = 't'
            else:
                turn = 'b'
        else:
            if n == 0:
                end = True
                break
            elif turn == 't':
                n -= 1
                top += 1
            else:
                n -= 1
                bottom -= 1
    if end == True:
        print('error')
    else:
        if turn == 't':
            print('[',end='')
            print(*arr[top:bottom],sep=',',end='')
            print(']')
        else:
            print('[',end='')
            print(*arr[top:bottom][::-1],sep=',',end='')
            print(']')
