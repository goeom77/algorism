T = int(input())
arr = []
for t in range(T):
    num = input().split()
    arr.append((int(num[0]),num[1]))
arr = sorted(arr,key=lambda x:x[0])
