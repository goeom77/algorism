# 시간 제한 1초
# 1 은 무조건 0
# 2는 0 하면 그대로 1은 앞학생과 바꾸기
# 뽑은 번호만큼 앞으로 가서 줄선다.
# 최종적으로 줄을 선 순서를 출력하기
# 학생 수
num = int(input())
# 바꿀 번호
arr = list(map(int, input().split()))
# 실제 번호
now = list(range(1, num+1))
result = []
# insert를 통해 원하는위치에 넣기
for i in range(1,num+1):
    result.insert(len(result) - arr[i-1],i)


print(*result,sep=" ")