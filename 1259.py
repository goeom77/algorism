a = 1
while a!=0:
    b = input()
    if b == '0':
        a = 0
    else:
        c = b[::-1]
        if b == c:
            print('yes')
        else:
            print('no')

