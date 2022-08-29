# 수 이어가기
# 두개의 양의 정수가 주어지고, 3번째 부터는 앞 2개의 차로 만든다.
# 음의 정수가 만들어지면 - 를 버리고 그만둔다.
a = int(input())
arr = list(range(a))
# 결과 넣을 리스트
result = []
for i in arr[::-1]:
    tmp = a - i
    compare = list()
    compare.append(a)
    compare.append(tmp)
    while tmp >= 0:
        tmp = compare[-2] - compare[-1]
        if tmp >= 0:
            compare.append(tmp)
        else:
            break

    if len(compare) > len(result):
        result = compare
print(len(result))
print(*result, sep=" ")