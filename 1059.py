from sys import stdin

arr_len = int(stdin.readline().rstrip())
arr = sorted(map(int,stdin.readline().rstrip().split()))
num = int(stdin.readline().rstrip())
now = 0
sorry = False
result = 0
for i in range(len(arr)):
    if num == arr[i]:
        sorry = True
        break
    if num < arr[i]:
        now = int(i)
        break
    if int(i) == int(len(arr))-1 :
        now = 100
if sorry == True:
    result = 0
else:
    if now == 0:
        min_num = num - 1
        max = arr[now]
        max_num = max - num -1
    elif now == 100:
        max_num = 1000 - num
        min = arr[- 1]
        min_num = num - min -1  
    else:
        max = arr[now]
        min = arr[now - 1]
        max_num = max - num -1
        min_num = num - min -1
    result = max_num + min_num + (max_num*min_num)
print(result)
