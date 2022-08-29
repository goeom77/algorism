# 테스크 케이스
from collections import deque
T = int(input())
for t in range(T):
    # 문서의 개수, 몇번째로 인쇄된지 궁금한 문서 index
    num, idx = map(int,input().split())
    # 맨 왼쪽이 0번째, 중요도 나열
    im = list(map(int,input().split()))
    #문서의 개수는 100이하
    s = im[idx]
    # 정렬한 것 처럼 pop시켜야 한다.
    w = sorted(im, reverse=True)
    im = deque(im)
    while im:
        for i in range(num):
            if w[i] == im[0]:
                im.popleft()
            