from heapq import heappush
n = int(input())

p = []
for t in range(n):
    p.append(int(input()))
if n ==1:
    result = 0
elif max(p) == p[0]:
    for i in range(1,n):
        if p[i] == p[0]:
            result = 1
            break
    else:
        result = 0
else:
    result = 0
    while True:
        h = []
        for i in range(n):
            a = p[i]
            heappush(h,(-a,a))
        if h[0][1] != p[0]:
            idx = p.index(max(p))
            p[idx] = p[idx] - 1
            p[0] = p[0] + 1
        else:
            break
        result += 1
    for i in range(1,n):
        if p[0] == p[i]:
            result += 1
            break
print(result)