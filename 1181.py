T = int(input())
sajun = []
for t in range(1,T+1):
    a = input()
    if [len(a),a] not in sajun:
        sajun.append([len(a),a])
sajun.sort()
sajun = tuple(sajun)
sajun = list(sajun)
for i in range(len(sajun)):
    print(sajun[i][1])