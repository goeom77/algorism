# 트리 순회
n = int(input())
# 노드 개수
base = ord('A')
node1 = [-1]*n
node2 = [-1]*n
for i in range(n):
    a,b,c = input().split()
    node1[ord(a)-base] = ord(b)-base
    node2[ord(a)-base] = ord(c)-base
# A가 항상 루트노드
f = []
i = []
ba = []
def front(n):
    f.append(chr(n+base))
    a = node1[n]
    if a != -19:
        front(a)
    b = node2[n]
    if b != -19:
        front(b)
front(0)
def init(n):
    a = node1[n]
    if a != -19:
        init(a)
    i.append(chr(n+base))
    b = node2[n]
    if b != -19:
        init(b)
init(0)
def back(n):
    a = node1[n]
    if a != -19:
        back(a)
    b = node2[n]
    if b != -19:
        back(b)
    ba.append(chr(n+base))
back(0)
print(*f,sep='')
print(*i,sep='')
print(*ba,sep='')
