
T = int(input())
for t in range(1,T+1):
    arr = list(map(int, input().split()))
    num = 10
    count = 0
    for i in range(1<<num):  # num의 부분함수 num개
        sum = 0
        for j in range(num): # 원소의 수만큼 비트를 비교
            if i & (1<<j):  # i의 j번 비트가 1인경우
                sum += arr[j]  # j번 비트를 더한다.
        if sum == 0:  # 부분함수들의 합의 개수 계산
            count += 1
    count -= 1   # 공집합 제거
    if count > 0:
        result = 1
    else:
        result = 0
    print(f'#{t} {result}')
