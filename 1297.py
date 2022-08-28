# TV의 크기 대각선 길이
# 가로 세로 비율 보내옴
# d 대각선, h, w 높이 너비 비율
# 소수가 나온경우 그수보다 작으면서 가장 큰 정수로 출력
d, h, w = map(int,input().split())
a = (d**2 / (h**2 + w**2))**(1/2)
r_h , r_w = int(h*a), int(w*a)
print(r_h, r_w)
