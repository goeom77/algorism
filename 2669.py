# 직사각형의 차지하는 면적
# 좌하, 우상 1~100
# 좌하를 사각형의 너비로 계산한다면 편안
data = [[0] * 101 for _ in range(101)]
for t in range(4):
    a, b, c, d = map(int, input().split())
    for j in range(b, d):
        for i in range(a, c):
            data[j][i] = 1
result = 0
for k in range(101):
    result += sum(data[k])
print(result)