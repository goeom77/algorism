# 1일 1달 3달 1년
T = int(input().rstrip())
for t in range(1,T+1):
    fare = list(map(int,input().split()))
    month = list(map(int,input().split()))
    c = []
    for i in month:
        c.append(min(fare[0]*i,fare[1],fare[2]))
    d = c + [0]*4
    for j in range(2,12):
        if (d[j] + d[j-1] + d[j-2]) > fare[2]:
            if d[j-2] >= d[j+1] and d[j-1] >= d[j+2]:
                d[j-2],d[j-1],d[j] = fare[2],0,0
    e = c + [0]*2
    for j in range(2,12):
        if (e[j] + e[j-1] + e[j-2]) > fare[2]:
            e[j-2],e[j-1],e[j] = fare[2],0,0

    result = min(sum(d),fare[3],sum(e),sum(c))
    print(f'#{t} {result}')