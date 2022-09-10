# RGB거리
# n = 집개수
# 집은 빨 초 파 비용
# 옆집과 색이 다르게 배치
# import sys
# n = int(input())
# # 3*2*2 의 개수의 다양성을 가지니깐 각자 계산해서 가장 최소의 값을 구해야한다.
# # 브르투포스로 모두 확인해야한다.
# color = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# cost = 1000000

# # 1번집 idx = 0
# def search_idx(idx,m,oder):
#     oder += 1
#     r_oder = oder-1
#     global cost
#     if oder == n:
#         tmp = m + color[r_oder][int(idx[r_oder])]
#         if tmp < cost:
#             cost = tmp
#         return
#     else:
#         if idx[r_oder] == '0':
#             tmp = m + color[r_oder][0]
#             if tmp > cost:
#                 return
#             else:
#                 return search_idx((idx+'1'),tmp,oder),search_idx((idx+'2'),tmp,oder)
#         elif idx[r_oder] == '1':
#             tmp = m + color[r_oder][1]
#             if tmp > cost:
#                 return
#             else:
#                 return search_idx((idx+'0'),tmp,oder),search_idx((idx+'2'),tmp,oder)
#         else:
#             tmp = m + color[r_oder][2]
#             if tmp > cost:
#                 return
#             else:
#                 return search_idx((idx+'0'),tmp,oder),search_idx((idx+'1'),tmp,oder)
# for i in range(3):
#     search_idx(str(i),0,0)
# print(cost)
nx = {0:[1,2], 1:[0,2], 2:[0,1]}

hold = [0,0,0]

N = int(input())
for i in range(N):
  cost = [int(x) for x in input().split()]
  for j in range(3):
    cost[j]+=min(hold[nx[j][0]], hold[nx[j][1]])
  hold = cost

print(min(cost))
