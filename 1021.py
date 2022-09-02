from collections import deque
# 숫자 n, 뽑아내려는 수 개수
n , m = map(int,input().split())
# 1. 뽑아내는 숫자(순서대로)
arr = list(map(int,input().split()))
# 인덱스를 확인해보고 앞과 뒤중에서 어디가 큰지를 확인해서  rotate로 돌리자
num_lst = list(range(1,n+1))
num_lst = deque(num_lst)
g = len(num_lst) - 1
result = 0
# g를 한개씩 감소시켜서 길이를 측정하는 시간을 줄이자
for i in arr:
    cnt = 0
    idx = num_lst.index(i)
    if g - idx < idx :
        num_lst.rotate(g-idx+1)
        num_lst.popleft()
        cnt = g - idx + 1
    else:
        num_lst.rotate(-idx)
        num_lst.popleft()
        cnt = idx
    g -= 1
    result += cnt
print(result)