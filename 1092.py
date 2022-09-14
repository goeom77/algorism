# 배
# 모든 화물은 박스에 있고 크렌인은 n대 1분에 하나씩 싣기 가능
# 각 크레인은 무게 제한있다.  시간의 최솟값은?
# 크레인 개수
import sys
n = int(input())
crane = list(map(int, sys.stdin.readline().split()))

b = int(input())
w = list(map(int, sys.stdin.readline().split()))
max_val = 0
min_val = 1000000
for i in range(b):
    if w[i] > max_val:
        max_val = w[i]
    if w[i] < min_val:
        min_val = w[i]




# box를 crane개수만큼 보여주고 만약 못든다면 옮긴 개수만큼만 이동해서 다시 들기
ck = [0]*b
total = 0
# 옮긴것은 ck를 1로 표시하자
# 작은것으로 무거운것을 들수 있는지 확인하는 기준

cnt = 0
if max(crane) < max_val:
    print('-1')
else:
    while total != b:
        # 크레인의 사용 유무 한번 옮기고 나서 reset
        use = [0]*n
        minus = 0
        while 



        for i in range(b):
            for j in range(n):
                # 크레인을 사용안 한것이고
                if not use[j]:
                    # 아직 옮기지 않은 박스인데 크레인으로 들수 있다면
                    if not ck[i] and crane[j] >= w[i]:
                        use[j] = 1
                        ck[i] = 1
                        total += 1
                        break
        # 한번씩 들었다면
        cnt += 1
print(cnt)