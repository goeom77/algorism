T = int(input())
for t in range(T):
    a,b = map(int,input().split())
    result = 1
    devide = 1
    # 54321/ 21 * (5-2)(5-3)(5-4)
    for i in range(b,a,-1):
        result *= i
    for j in range(1,b-a+1):
        devide *= j
    rresult = int(result/devide)
    print(rresult)