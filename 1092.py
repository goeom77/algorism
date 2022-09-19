# 배
# 모든 화물은 박스에 있고 크렌인은 n대 1분에 하나씩 싣기 가능
# 각 크레인은 무게 제한있다.  시간의 최솟값은?
# 크레인 개수
import time
start = time.time()
import sys
n = int(input())
crane = list(map(int, sys.stdin.readline().split()))
# 50개니깐 sort하고 그 간격만큼 위에 있는 크레인이 처리하는 용도로 사용하자
# 같은 것도 있으니깐 고려
crane.sort()
b = int(input())
w = list(map(int, sys.stdin.readline().split()))
game = True
# 각 크레인 보다 무거운 것이 몇개 있는지 확인하고 
# 각자의 최솟값만큼 처리한 다음 다른 크레인이 밑의 짐들을 지원하는 방법으로 처리하자
possible = [0]*n
extra = 0
for j in range(b):
    for i in range(1,n):
        # 숫자가 같은 크레인은 어떻게 처리해야 할까?
        if crane[i-1] < w[j] <= crane[i]:
            possible[i] += 1
            extra +=1
        elif w[j] > crane[n-1]:
            game = False
possible[0] = b - extra
ability = [1]*n
while True:
    for i in range(n):
        if possible[i] == 0 and ability[i] != 0:
            ability[i] = 0
            ability[i-1] += 1
    while True:
        for i in range(n):
            if possible[i] == 0 and ability[i] != 0:
                break
        


print("time:", time.time() - start,'sec')
