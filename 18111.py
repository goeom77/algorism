# 마인 크래프트
# 땅고르기가 필요 세로n가로 m인 집터 왼쪽위가 (0,0)이다.
# 블록 제거 2초 쌓기 1초
# 기본 들고있는 블록 b
# 땅 높이 256최대 음수 불가


import sys
n,m,b = map(int, sys.stdin.readline().split())
land = []
# 답이 여러개면 땅 높이 가장 높은 것으로 출력
max_b = 0
min_b = 256
sum_b = 0
for j in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    if max_b > max(a):
        max_b = max(a)
    if min_b < min(a):
        min_b = min(a)
    sum_b += sum(a)
    land.append(a)
# 파는 것은 끝까지 팔수 있어도 체우는건 한계가 있으니깐
limit = (sum_b + b)//(n*m)
if limit <= max_b:
    max_b = limit
result_time = 256*n*m*2
result_land = 0
for k in range(min_b,max_b+1):
    time = 0
    for j in range(n):
        for i in range(m):
            if k > land[j][i]:
                time += (k-land[j][i])
            elif k< land[j][i]:
                time += 2*(land[j][i]-k)
    if result_time > time:
        result_time = time
        result = k
    elif result_time < time:
        break
print(f'{result_time} {result_land}')
# high = 0 # 땅의 가장 평균 높이
# for i in range(n):
#     high += sum(land[i])
# extra = n*m - high%(n*m) # 체워야 되는 블럭수
# high = high//(n*m)
# soar = b//(n+m)

# # high ~ high + 1 + b/(n*m)개 검색
# if extra > b: # 블럭으로 체워넣을 수 없는 경우 원천 차단
#     high += 1
# ck = True
# result_time = 256*n*m*2
# result = 0
# for k in range(high,high+soar+2):
#     time = 0
#     for j in range(n):
#         for i in range(m):
#             if k > land[j][i]:
#                 time += (k-land[j][i])
#             elif k< land[j][i]:
#                 time += 2*(land[j][i]-k)
#     if result_time >= time:
#         result_time = time
#         result = k
#     elif result_time <time:
#         break

# print(f'{result_time} {result}')