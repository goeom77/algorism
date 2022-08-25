T = int(input())
arr = []
for t in range(T):
    arr.append(input().rstrip())
arr = set(arr)
arr = list(arr)
n = len(arr)
brr = arr[:]
for i in range(n):
    for j in range(n):
        if j != i:
            m = len(j)
            if arr[j][:m] in arr[i] and arr[i][0] == arr[j][0]:
                brr.remove(arr[j])
result = len(brr)
print(result)