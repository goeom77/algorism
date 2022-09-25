# 10815 숫자카드
# 정수 하나가 적혀 있는 카드 n개
# 정수 m개 주어져있을 때 상근이가 가지고 있는건지 구하는 프로그램
import sys
from collections import defaultdict
n = int(input()) #1~500000
my_card = list(map(int, sys.stdin.readline().split()))
my = defaultdict(int)
for i in range(n):
    my[my_card[i]] += 1
m = int(input())
ck_card = list(map(int, sys.stdin.readline().split()))
for i in range(m):
    if my[ck_card[i]] > 0:
        print(1,end=" ")
    else:
        print(0,end=" ")
print()