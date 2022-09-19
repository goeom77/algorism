# 리모컨
# 리모컨 최소 횟수로 이동
# 지금 보는 건 100번
# 0에서 -눌려도 0이다.
# 0~500,000
op = input()
# 고장난 버튼 개수
x = int(input())
x_list = list(map(int, input().split()))
remocon = [1]*10
for i in range(x):
    remocon[x[i]] = 0

# 그 자리에서 가장 가까운 값 찾기
def set_number(x):
    cnt_h = 0
    cnt_l = 0
    while True:
        cnt_h += 1
        if remocon[(a+cnt_h)%10]==1:
            break
    while True:
        cnt_l += 1
        if remocon[a-cnt_l]==1:
            break
    if cnt_h > cnt_l:
        
    return min(cnt_h,cnt_l)

def 
# [0,1,2,3,4,5,6,7,8,9] 번 중에서
# [1,1,1,1,1,1,0,0,0,1] 을 사용가능
result = ''

# +, - 만 이용해서 갈수 있는 case
if 102>= int(op) >= 98:
    print(abs(int(op)-100))
else:
    opp = list(op)
    if len(opp) == 1:
        a = int(op)
        if remocon[a] == 1:
            print(1)
        else:
            
    # 숫자가 둘이상일 때는 반올림해서 근사값으로 가야한다.
    else:
        if len(opp) == 2:
