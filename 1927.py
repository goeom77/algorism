# 최소 힙
# 1. 배열에 자연수 x를 넣는다
# 2. 배열에서 가장 작은 값을 출력하고, 그값을 배열에서 제거한다.
n = int(input())
from heapq import heappush, heappop
import sys

h = []
for i in range(n):
    a = int(sys.stdin.readline())
    if not a:
        if h:
            b = heappop(h)
            print(b)
        else:
            print(0)
    else:
        heappush(h,a)
