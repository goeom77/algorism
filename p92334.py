# n발 쏜다.
# 상대보다 크거나 같으면 라이언이 k점 얻는다.
n = int(input()) # 1~10발
# 과녘 맞춘 개수
info = list(map(int,input().split())) # 0~10점까지
# 라이언이 가장 큰 점수차로 이기기 위한 방법 찾기
result = -1
result_arr = []
def perm(n,m,k):
    global result
    if n==m:
        if sum(choice) == k:
            print(choice[:])
            cnt = 0
            for i in range(11):
                if choice[i] >= info[i]:
                    cnt += i
                else:
                    cnt -= i
            if cnt > result:
                result = cnt
                result_arr = choice[:]
        return
    for i in range(len(arr)):
        choice[n] = arr[i]
        perm(n+1,m,k)


arr = list(range(11))
choice = [0]*(11)
perm(0,10,n)
if result <0:
    print('[-1]')
else:
    print(result_arr)







