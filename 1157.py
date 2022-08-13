arr = input().upper()
brr = set(arr)
lst_brr = []
for i in brr:
    sum = arr.count(i)
    lst_brr.append([sum,i])
lst_brr.sort(reverse=True)
if len(arr) == 1:
    print(arr)
elif lst_brr[0][0] == lst_brr[1][0]:
    print('?')
else:
    print(lst_brr[0][1])
