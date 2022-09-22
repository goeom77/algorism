
# 5189 - 전자카트
# 사무실에서 출발해 한번씩만 방문하고 사무실로 돌아올때 최소 배터리 사용량
# 1 사무실 2,3 관리구역

def path(num,visited,total):
    # num은 몇개를 체웠는지, visited는 들린곳인지, total은 완성된 path경로
    global n
    for i in range(2,n+1):
        if not visited[i]:
            num += 1
            visited[i] = True
            total += str(i)
            if num == n:
                total += '1' # 마지막에 1을 들려야 하니깐
                result.append(total)
            path(num,visited,total)
            num -= 1
            visited[i] = False
            total = total[:-1]
            
    # visited를 n-1개 순서대로 넣고 싶으면?


T = int(input())
for t in range(1,T+1):
    # 사무실 + 관리구역 개수(3~10)
    n = int(input())
    using = [list(map(int, input().split())) for _ in range(n)]
    # path = 경로 경우의 수
    visited = [1] + [0]*n # 0은 없으니깐 체워놓기
    visited[1] = True     # 시작포인트니깐
    result = []           # 1231 1321 경로추가
    path(1,visited,'1')
    end = []
    for i in range(len(result)):# result개수만큼 비교
        temp = 0
        for j in range(n):
            temp += using[int(result[i][j])-1][int(result[i][j+1])-1]
        end.append(temp)
    print(f'#{t} {min(end)}')