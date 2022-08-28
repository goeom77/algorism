# 종이 자르기
# 가장 큰 종이의 넓이를 구하시오
# 가로 세로 길이 <= 100
m, n = map(int,input().split())
# 칼로 잘라야하는 점선 개수
T = int(input())
m_data = [0,m]
n_data = [0,n]
for t in range(T):
    # 가로로 자를떄는 0 세로로 자를때는 1
    a, b = map(int, input().split())
    if a == 0:
        n_data.append(b)
    else:
        m_data.append(b)
# 자른 것과 크기를 기준으로 정렬을 해서 크기를 측정
m_data.sort()
n_data.sort()
mx_m = 0
mx_n = 0
for i in range(1, len(m_data)):
    tmp = m_data[i] - m_data[i-1]
    if mx_m < tmp:
        mx_m = tmp
for i in range(1, len(n_data)):
    tmp = n_data[i] - n_data[i-1]
    if mx_n < tmp:
        mx_n = tmp
result = mx_m * mx_n
print(result)