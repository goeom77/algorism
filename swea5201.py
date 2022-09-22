
# n개의 컨테이너를 m대의 트럭으로 운반
# 최대 한개 운반 가능
# 화물 무게, 트럭 적재용량 주어진다. 
# 화물의 총 중량이 최대가 되도록 했을 때 옮겨진 화물의 전체 무게 출력
T = int(input())
for t in range(1, T+1):
    n,m = map(int, input().split())
    weight = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    move = [0] * n
    # 옮긴 것은 1로 확인
    total = 0
    for i in range(m):
        tmp = (0,0)
        for j in range(n):
            if not move[j] and weight[j] <= truck[i] and weight[j] > tmp[0]:
                tmp = (weight[j], j)          # 안 옮긴 짐이고, 무게가 작거나 같으면서 최대값인것
        if tmp == (0,0):                      # 들수 있는것이 없을 때는 계산 하지 않는다.
            continue
        total += tmp[0]                       # 선정된 짐의 무게를 최종 결과에 더한다.
        move[tmp[1]] = 1                      # 옮긴 것이라고 표시한다.
    print(f'#{t} {total}')