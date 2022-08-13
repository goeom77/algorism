# a = input()
# arr = list()
# brr = list()
# for i in a:
#     arr.append(int(i))
# arr.sort(reverse=True)
# for j in arr:
#     brr.append(str(j))
# crr = "".join(brr)
# print(crr)

arr = input()
for i in range(9,-1,-1):
    for j in arr:
        if int(j) == i:
            print(i,end='')