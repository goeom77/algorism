for a in range(10):
    t = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    max = 0
    for i in range(100):
        sum = 0
        for j in range(100):
            sum += arr[i][j] # 행의 합 구하기
        if sum > max:
            max = sum
    for i in range(100):
        sum = 0
        for j in range(100):
            sum += arr[j][i] # 열의 합 구하기
        if sum > max:
            max = sum
    sum = 0
    for i in range(100): # 정 대각선의 합 구하기
        sum += arr[i][i]
    if sum > max:
        max = sum
    sum = 0
    for i in range(100): # 역 대각선의 합 구하기
        sum += arr[i][99-i]
    if sum > max:
        max = sum
    print(f'#{t} {max}')