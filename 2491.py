# 크거나 같은 것 먼저 검색
num = int(input())
arr = [0] * (num - 1)
# 숫자가 한개인 경우 1로 발생해야 하기 때문에 부여한다.
if num <2:
    print(num)
# 메모리즘을 통해 리스트를 저장한다.
else:
    data = list(map(int,input().split()))
    cnt = 1
    for i in range(1,num):
        if data[i-1] <= data[i]:
            cnt += 1
            arr[i-1] = cnt
        else:
            cnt = 1
    tmp1 = max(arr)
    brr = [0] * (num - 1)
    cnt = 1
    for i in range(1,num):
        if data[i-1] >= data[i]:
            cnt += 1
            brr[i-1] = cnt
        else:
            cnt = 1
    tmp2 = max(brr)
    result = max(tmp1,tmp2)
    print(int(result))