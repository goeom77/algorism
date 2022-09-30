# 로또 번호 선택
# k개의 수중 6개의 수로 이루어진 조합을 만드는 것
def comb(n,m,j):
    if n==m:
        print(*chosen)
        return
    for i in range(j, len(lst)):
        chosen[n] = lst[i]
        comb(n+1,m,i+1)

while True:
    a, *lst = map(int, input().split())
    if a == 0:
        break
    else:
        print()
    arr= []
    chosen = [0]*6
    comb(0,6,0)
