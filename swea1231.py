# 10개의 테스트
# n = 정점 개수;
# 정점 정보 : 문자, 왼쪽 자식, 오른쪽 자식 순서로 준다.
def inorder(n):                                                  
    if n:
        inorder(ch1[n])
        print(arr[n],end='')
        inorder(ch2[n])

for t in range(1, 11):
    n = int(input())
    arr = [None] * (n+1)
    ch1 = [0] * (n+1)
    ch2 = [0] * (n+1)
    for i in range(n):
        a,b,*c = input().split()
        a = int(a)
        arr[a] = b
        if len(c):
            ch1[a] = int(c[0])
        if len(c) ==2:
            ch2[a] = int(c[1])
    print(f'#{t} ')
    inorder(1)
    print()
    
