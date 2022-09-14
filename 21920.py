# 서로소
# 길이가 n인 A에서 x와 서로소인 수의 평균 구하기
n = int(input())
a = list(map(int, input().split()))
x = int(input())
cnt = 0
result = 0
for i in range(n):
    if a % x != 0 and x % a != 0:
        
        
