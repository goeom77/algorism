# 베이비진 게임
# 0~9까지 4세트 6개뽑았을 때 
# 연속 3개 이상 run, 같은 숫자 3개 이상 triple
# one two 한개씩 카드 가져간다.
# 무승부는 0출력(둘다 안된경우)
T = int(input())
for t in range(1, T+1):
    # 한사람당 최대 6장을 받는다.
    card = list(map(int, input().split()))
    # one win = 1 two win= 2 draw = 0
    one = []
    two = []
    win = 0
    for i in range(12):
        if not i%2:
            one.append(card[i])
        else:
            two.append(card[i])
            one.sort()
            two.sort()
            if i >= 5:
                for j in range(2,(i//2)+1):
                    if one[j] == one[j-1] == one[j-2]: # triple인 케이스
                        win = 1
                        break
                    elif one[j] == one[j-1]+1 == one[j-2] +2: # run인 케이스
                        win = 1
                        break
                    elif j>=3 and one[j] == one[j-2]+1 == one[j-3] + 2: # 한칸 띄고 triple
                        win = 1
                        break
                    elif j>=3 and one[j] == one[j-1]+1 == one[j-3] + 2: # 한칸 띄고 triple
                        win = 1
                        break
                    elif not win and two[j] == two[j-1] == two[j-2]:  # 1이 이기지 못했을때
                        win = 2
                        break
                    elif not win and two[j] == two[j-1] +1  == two[j-2]+2:
                        win = 2
                        break
                    elif not win and j>=3 and two[j] == two[j-2]+1 == two[j-3] + 2:
                        win = 2
                        break
                    elif not win and j>=3 and two[j] == two[j-1]+1 == two[j-3] + 2:
                        win = 2
                        break
        if win:
            break
    print(f'#{t} {win}')
   