T = int(input())
arr = list(input())
sum = 0
for i in range(T):
    num = ord(arr[i])-96
    sum += num * (31**i)

print(sum%1234567891)