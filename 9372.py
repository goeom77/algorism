# n개국 여행
# 최대한 적은 종류의 비행기를 타려고 한다.
# 이동시 거쳐가는것 가능
# T = int(input())
# for t in range(T):
# n = 국가의 수, m = 비행기 종류
n, m = map(int, input().split())
for i in range(m):
    # 비행기 일정 a, b쌍 1<= a, b <= n
    # a, b를 왕복하는 비행기가 있다.
    a, b = map(int, input().split())