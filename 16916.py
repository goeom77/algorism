import sys

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()
if a.count(b) > 0:
    print(1)
else:
    print(0)