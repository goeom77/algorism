t = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'1':0,'2':1,'3':2,'4':3,'5':4,'6':5}
visited = [[0]*6 for _ in range(6)]
for i in range(36):
    p = input()
    row = p[0]
    column = p[1]
    visited[t[column]][t[row]] = 1

all = True
for j in range(6):
    for i in range(6):
        if visited[j][i] == 0:
            all = False
if all:
    print('Valid')
else:
    print('Invalid')