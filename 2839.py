size = int(input())
result = 0
for i in range(1000,-1,-1):
    if (size -(5*i)) > 0:
        if (size -(5*i))% 3 == 0:
            b = (size-(5*i))/3
            result = i +b
            break
    else:
        if (size % 3) ==0:
            result = size /3
            break
if result == 0:
    print(-1)
else:
    print(result)
