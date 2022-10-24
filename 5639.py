c1 = [0]*1000001
c2 = [0]*1000001
root = int(input())
q = [root]
while True:
    try:
        a = int(input())
        if a < root:
            if c1[root] == 0:
                c1[root] = a
                q.append(a)
                break
            else:
                q.pop()

