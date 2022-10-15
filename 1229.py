# 육각수
INF = int(1e9)
n = int(input())
# 육각수를 통해 n을 만들기
arr = [1]
k = 1
tmp = 0
while k < n:
    tmp += 1
    k = tmp*4+1+arr[-1]
    arr.append(k)
# 백 트래킹으로 풀어보자
# result = INF
# cnt = n
# for j in range(len(arr)-1,-1,-1):
#     if cnt < arr[j]:
#         result += arr[j]//cnt
print(708**6)
