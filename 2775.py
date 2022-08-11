T = int(input())
for t in range(T):
    height = int(input())
    weight = int(input())
    h_people = []
    for i in range(1,weight+1):
        h_people.append(i)
    for j in range(height):
        count = 0
        for i in range(weight):
            count += h_people[i]
            h_people[i] = count
    if j == height-1:
        print(h_people[weight-1])