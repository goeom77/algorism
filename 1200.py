T = int(input())
a = []
for i in range(T):
    b = list(map(int,input().split()))
    a.append(b)
c = [0]*T
for j in range(T):
    for k in range(T-1):
        if (a[j][1]+1)*a[k][0] > (a[k][1]+1)*a[j][0]:
            c[j] += 1
        else:
            c[k] += 1
d = sorted(c)

for i in range(T):
    a = d.index(c[i])
    print(int(a)+1)
    