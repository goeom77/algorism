# 곱셈
# a를 b번 곱하고 c로 나눈 나머지를 구하기
a,b,c = map(int, input().split())
result = 1
for i in range(b):
    result *= a
    result %= c
print(result)