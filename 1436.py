
n = int(input())
save_point = '666'
ck = 0
while True:
    if n == 1:
        break
    if save_point[0] == 9:
        a,b =save_point.split('666')
        a = '10' + a[1:]
        save_point = a+'666'+b
        ck = 0
    elif save_point[0:3] == '666' and ck ==0:
        save_point = '1' + save_point
    elif '5666' in save_point:
        a,b = save_point.split('666')
        ck += 1
        a = a[:-1]
        b = b[:-1] + '0'
        save_point = a + '666' + b
    elif save_point[0] == '6':
        if b == '9'*len(b):
            a = a + '7'
            save_point = a + '666' + '0'*(len(b)-1)
            ck -= 1
        else:
            b = str(int(b)+1)
            save_point = a + '666' + b
    else:
        a,b = save_point.split('666')
        a = str(int(a)+1)
        save_point = a + '666' + b
    n-= 1
print(save_point)