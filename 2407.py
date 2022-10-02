n,m = map(int, input().split())
o = n-m
if o >m:
    m,o = o,m
arr = list(range(n,m,-1))
num = 1
for i in range(len(arr)):
    num *= arr[i]
for i in range(len(arr)):
    num//=(i+1)
print(int(num))
