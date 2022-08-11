# 0_counter = record[0]
# 1_counter = record[1]
T = int(input())
for i in range(T):
    record = [(1,0),(0,1)]
    num = int(input())
    if num < len(record):
        print(record[num][0],record[num][1])
    else:
        for j in range(num +1 - len(record)):
            a = int(record[-2][0]) + int(record[-1][0])
            b = int(record[-2][1]) + int(record[-1][1])
            c = (a,b)
            record.append(c)
            # print(record)
        print(record[num][0],record[num][1])
