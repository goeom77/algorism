# 1,2,3,4,5,6,
num = int(input())
x = y = 1
count = 1
while True:
    if count == num:
        break
    if x == 1:
        if y == 1:
            y += 1
            count += 1
        else:
            x += 1
            y -= 1
            count += 1
    if count == num:
        break
    if y == 1:
        y = x + 1
        x = 1
        count += 1
if (x+y) % 2:
    print(f'{x}/{y}')
else:
    print(f'{y}/{x}')