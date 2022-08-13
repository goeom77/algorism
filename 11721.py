arr = list(input())

while len(arr) >0 :
    if len(arr) >= 10:
        brr = []
        for i in range(10):
            brr.append(arr.pop(0))
            print(brr[i],end="")
        print()

    else:
        brr = []
        for i in range(len(arr)):
            brr.append(arr.pop(0))
            print(brr[i],end="")


