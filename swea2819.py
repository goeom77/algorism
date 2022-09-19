# 2819 숫자 이어붙이기
# 4*4 격자판이 있다.
# 0~9까지 숫자가 적혀있고 4방향 6번 이동해서 차례로 붙일 때 왔던곳 다시 갈수도 있다.
# 만들수 있는 서로 다른 일곱자리 수들의 개수를 구하는 프로그램을 작성하시오
# 브루트포스 방법으로 모두 탐색하는 방법으로 해보자 -> recursion error 나온다.
from collections import defaultdict
T = int(input())
for t in range(1,T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    # dp를 통해 해당 i,j에 대해서 나올수 있는 경우의 수와 idx를 넣자
    result = []
    def go(i,j,sentence,cnt):
        if cnt == 7: # 7개의 숫자가 쌓이게 되면 result에 함수를 넣고 그만둔다.
            if int(sentence) not in result:
                result.append(int(sentence))
        else:
            r_val = arr[j][i]
            for k in search[i,j,r_val]:
                go(k[0],k[1],sentence + str(k[2]),cnt+1) # 지나 갈때 마다 str을 갱신하고 cnt를 추가한다.


    search = defaultdict()
    # i,j,num : (ni,nj,num)
    for j in range(4):
        for i in range(4):
            value = arr[j][i]
            search[(i,j,value)] = [] # 딕셔너리 초기값 설정
            for dx,dy in [[1,0],[-1,0],[0,1],[0,-1]]: # 네방향을 모두 확인해서
                nx = dx + i
                ny = dy + j
                if nx < 0 or nx >= 4 or ny <0 or ny >= 4: # 격자 안에 있는 것으로
                    pass
                else:
                    r_value = arr[ny][nx]
                    search[(i,j,value)].append((nx,ny,r_value)) # 딕셔너리를 만든다.
    for j in range(4):
        for i in range(4):
            go(i,j,'',0)
    print(f'#{t} {len(result)}')
        
