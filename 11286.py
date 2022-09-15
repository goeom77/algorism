# 절댓값 힙
# x를 넣는다.
# 배열에서 절댓값이 가장 작은 값을 출력하고 그 값을 배열게서 제거한다.
# 가장작은 값이 여러개면 출력하고 그 값을 모두 제거

n = int(input())
from heapq import heappush, heappop
import sys

h = []
for i in range(n):
    a = int(sys.stdin.readline())
    if not a:
        if h:
            b = heappop(h)
            print(b[1])
        else:
            print(0)
    else:
        if a > 0:
            heappush(h,(a,a))
        else:
            heappush(h,(-a,a))
