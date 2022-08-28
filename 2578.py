# 1~ 25 빙고판 만든다.
# 부르는 수를 지울 때 빙고 처음 하면 이긴다.
# 몇번ㅉ에 빙고가 생기는지 확인
# 5번 까지는 0으로 만들고 경우의 수를 모두 확인해보자
# 빙고판
bingo = []
for i in range(5):
    bingo.append(list(map(int,input().split())))
result = False
# 숫자를 지우려면 index를 써야하나?
def chk(arr):
    global result
    cnt1 = 0
    cnt2 = 0
    for i in range(5):
        cnt = 0
        for j in range(5):
            if sum(arr[j]) == 0:
                result = True
                return
            elif arr[j][i] == 0:
                cnt += 1
            elif i == j:
                if arr[j][i] == 0:
                    cnt1 += 1
            elif i + j == 4:
                if arr[j][i] == 0:
                    cnt2 += 1
        if cnt == 5:
            result = True
            return
    if cnt1 == 5:
        result = True
        return
    elif cnt2 == 5:
        result = True
        return
for j in range(5):
    # 각 숫자의 인덱스를 기입하고 그것에 맞는 딕셔너리를 만들어서 임의의 빵판에 삭제를 하고 확인한다면?
    