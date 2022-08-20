import sys
from collections import defaultdict
num = int(input())
arr = sys.stdin.readline().rstrip().split()
arr_dict = {}
arr_dict = defaultdict(arr)
print(arr_dict)
