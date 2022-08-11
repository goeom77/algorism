T=2
m,n,num = map(int,input().split())

count = 0
a=[]
for k in range(m):
    a.append([0]*n)
for i in range(num):
    x,y = map(int,input().split())
    a[x][y] = 1
for xx in range(1,m):
    for yy in range(1, n):
        if a[xx][yy] == 1:
            if a
