# IQ Test

n = int(input())
arr = list(map(int, input().split()))
# num*a + b
a = 0
b = 0
result = []
if n == 1:
    result.append('a')
    result.append('b')
else:
    for i in range(-1000,1000):
        k = arr[1] - arr[0]*i
        cnt = 0
        for j in range(1,n):
            if arr[j-1]*i + k == arr[j]:
                cnt += 1
            else:
                break
        if cnt == n-1:
            b = k
            a = i
            value = arr[-1]*a + b
            result.append(value)
        if len(result) >= 2:
            break
        
result = list(set(result))
if len(result) >= 2:
    print('A')
elif len(result) == 0:
    print('B')
else:
    print(result)