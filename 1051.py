n,m = map(int,input().split())

arr = [list(map(int,input())) for _ in range(n)]

if n> m:
    arr = list(zip(*arr))
    n, m = m,n


size = n
result = False
value = 0
if n == 1:
    result = True
    value = 1
while result != True:
    idx_n = n - size + 1
    idx_m = m - size + 1
    for i in range(idx_n):
        for j in range(idx_m):

            temp = arr[i][j]
            if arr[i+size-1][j] == temp and arr[i][j+size-1] == temp and arr[i+size-1][j+size-1] == temp:
                result = True
                value = size
                break
        if result:
            break
    size -= 1

print(value*value)

