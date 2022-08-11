T = int(input())
a = int(input())
b = []
result = 0
for t in range(T-1):
    b.append(int(input()))
if T ==1:
    result = 0
else:
    while max(b)>= a:
        b[b.index(max(b))] -=1
        a+=1
        result +=1


print(result)