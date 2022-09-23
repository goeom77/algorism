# 1~n 사람 번호
# i 번 사람 돈 일출 시간 pi
# 줄 서는 순서에 따라 합이 달라진다.
t = int(input())
arr = list(map(int,input().split()))
arr.sort()
total = 0
for i in range(t):
    total += arr[i]*(t-i)
print(total)