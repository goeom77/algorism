from collections import deque
# R빨 G초 B파
# 적록 색맹은 빨 초 같은걸로 본다.
n = int(input())
arr = [list(input()) for _ in range(n)]
no_sek = [[0]*n for _ in range(n)]
sek = [[0]*n for _ in range(n)]
# visited를 이용해서 bfs사용
no_sek_visited = [[0]*n for _ in range(n)]
sek_visited = [[0]*n for _ in range(n)]
# 빨 2 초 1 파 0
# 빨초 = 1 파 = 0
for j in range(n):
    for i in range(n):
        if arr[j][i] == 'G':
            no_sek[j][i] = 1
            sek[j][i] = 1
        elif arr[j][i] == 'R':
            no_sek[j][i] = 2
            sek[j][i] = 1
no_sek_cnt = 0
no_sek_q = deque()
sek_cnt = 0
sek_q = deque()
for j in range(n):
    for i in range(n):
        if no_sek_visited[j][i] == 0:
            no_sek_cnt += 1
            no_sek_q.append((j,i))
            no_sek_visited[j][i] = 1
            # 있으면 1 없으면 0
            while no_sek_q:
                sj,si = no_sek_q.popleft()
                for ki,kj in [[0,-1],[0,1],[1,0],[-1,0]]:
                    sjj,sii = sj + kj, si + ki
                    if 0<=sjj<n and 0<=sii<n and no_sek_visited[sjj][sii] == 0 and no_sek[sj][si] == no_sek[sjj][sii]:
                        no_sek_q.append((sjj,sii))
                        no_sek_visited[sjj][sii] = 1
        if sek_visited[j][i] == 0:
            sek_cnt += 1
            sek_q.append((j,i))
            sek_visited[j][i] = 1
            while sek_q:
                nj, ni = sek_q.popleft()
                for ki,kj in [[0,-1],[0,1],[1,0],[-1,0]]:
                    njj,nii = nj + kj, ni + ki
                    if 0<=njj<n and 0<=nii<n and sek_visited[njj][nii] == 0 and sek[nj][ni] == sek[njj][nii]:
                        sek_q.append((njj,nii))
                        sek_visited[njj][nii] = 1
print(no_sek_cnt,sek_cnt,end=" ")
