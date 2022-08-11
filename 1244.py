light = int(input())
arr = list(map(int,input().split()))
people = int(input())

for t in range(people):
    a,b = map(int,input().split())
    c = d = 0
    if a == 1:
        temp = light//b
        for i in range(1,temp+1):
            ii = input(i)
            a[str(ii)] += 1
        print(arr)
    else:
        arr[b-1] += 1
        count = 0
        while c != d:
            if arr[b-1-count] == arr[b-1+count]:
                if arr[b-1-count] == 1:
                    arr[b-1-count] = arr[b-1+count] = 0
                else:
                    arr[b-1-count] = arr[b-1+count] = 1
            else:
                d = 1
    
for k in range(len(arr)):
    arr[k] = int(arr[k]) % 2


# if len(arr)> 20:
#     result1 = ''.join(arr[0:20])
#     print(result1)
# elif len(arr) >40:
#     result2 = ''.joing(arr[20:40])
#     print(result2)
# elif len(arr) >60:
#     result3 = ''.joing(arr[40:60])
#     print(result3)
# elif len(arr) >80:
#     result4 = ''.joing(arr[60:80])
#     print(result4)
# else:
#     result5 = ''.joing(arr[80:])
#     print(result5)  

