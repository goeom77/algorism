# ACM craft
# t 테스트 케이스
T = int(input())
for t in range(T):
    # n = 건물의 개수 k = 규칙 수
    n, k = map(int, input().split())
    # 건물 건출 시간
    time = list(map(int, input().split()))
    law = [[0]*n]
    for i in range(k):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        if law[a][0] == 0:
            law[a][0] = b
        else:
            law[a].append()
