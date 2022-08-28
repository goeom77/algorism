# 가로, 세로 길이
m, n = map(int, input().split())
# 상점들의 idx
idx = []
# 상점 개수
t = int(input())
for i in range(t+1):
    #북서의 모서리를 기준으로 하나의 선을 만든다.
    a, b = map(int, input().split())
    if a == 1:
        idx.append(b)
    elif a == 2:
        idx.append(-n-b)
    elif a == 3:
        idx.append(-b)
    else:
        idx.append(m+b)
# 동근이 위치
dong = idx.pop()
# 거리 구하기
result = 0
mx = 2*m + 2*n
for i in idx:
    # 인코스, 아웃코스 두가지를 구해서 최소값을 넣자
    t1 = abs(i - dong)
    t2 = mx - t1
    result += min(t1,t2)
print(result)
