T = int(input())
arr = []
for t in range(T):
    num = int(input())
    arr.append(num)

arr.sort()

for i in arr:
    print(i)