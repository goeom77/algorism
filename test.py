N, M = map(int, input().split())
lst = [list(input()) for _ in range(N)]
mm = min(N, M)
MM = max(N, M)
if mm == M:
    lst = list(zip(*lst))
result = 1
temp = False
for j in range(0, mm - 1):
    size = mm - j
    for k in range(MM - j + 1):
        for x in range(mm -j +1):
            if lst[k][x] == lst[k + mm - j -1][x] == lst[k][x + mm - j -1] == lst[k + mm - j -1][x + mm - j -1]:
                result = mm - j
                temp = True
                break
        if temp == True:
            break
    if temp == True:
        break

print(result * result)