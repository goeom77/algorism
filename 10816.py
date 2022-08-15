# 카드 개수
# 숫자 카드
# 구해야할 숫자카드 개수
# 구해야할 숫자카드 -> 각각의 개수 알아야한다.
import sys
from collections import defaultdict

card_num = int(input())
card_cnt = list(map(int,sys.stdin.readline().rstrip().split()))
op_num = int(input())
op_cnt = list(map(int,sys.stdin.readline().rstrip().split()))
result = {}
result = defaultdict(lambda: 0)
for i in card_cnt:
    result[i] += 1

for j in op_cnt:
    if result[j] == None: print(0,end=" ")
    else:
        print(result[j],end=" ")