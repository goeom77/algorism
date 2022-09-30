# 2108 통계학
# 산술평균 n개 수 합을 n으로 나누기
# 중앙값 n개 나열시 중앙 위치 값
# 최빈값 n개 수중 가장 많은 값 똑같은게 여러개면 작은값중 2번째
# 범위 n개 수의 최대와 최소 차이
import sys

n = int(input())

arr = [0]*8001 # 0~8000 -4000 ~ 4000 

total = 0
for i in range(n):
    num_get = int(sys.stdin.readline().rstrip())
    # 산술 평균
    total += num_get
    # 중앙값, 최빈값, 범위
    arr[num_get+4000] += 1
# n은 홀수 이니깐 중앙값은 n//2+1이 된다.
tmp = 0
middle = n//2+1
middle_ck = True
max_cnt = 0
low = True
low_value = 0
high_value = 0
for i in range(8001):
    tmp += arr[i]
    if middle_ck and tmp >= middle:
        middle_ck = False
        middle = i-4000
    if arr[i] > max_cnt:
        max_cnt = arr[i]
    if low and arr[i] >0:
        low = False
        low_value = i-4000
    if arr[i]>0:
        high_value = i-4000
how_much = []
for i in range(8001):
    if arr[i] == max_cnt:
        how_much.append(i-4000)
# 산술평균
print(int(round(total/n,0)))
# 중앙값
print(middle)
# 최빈값
if len(how_much) == 1:
    print(how_much[0])
else:
    print(how_much[1])
# 범위
print(high_value-low_value)

    



