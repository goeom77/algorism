# 강의실 배정
# s -> T 에 끝나는 n개 수업
# 최소의 강의실로 모든 수업 가능하게 s==T같으면 수업 가능
n = int(input())
# 1~200000
for i in range(n):
    s, t = map(int, input().split())