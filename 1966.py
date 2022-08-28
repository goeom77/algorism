# 테스크 케이스
T = int(input())
for t in range(T):
    # 문서의 개수, 몇번째로 인쇄된지 궁금한 문서 index
    num, idx = map(int,input().split())
    # 맨 왼쪽이 0번째, 중요도 나열
    im = list(map(int,input().split()))
    #문서의 개수는 100이하
    s = im[idx]
    im.sort(reverse=True)
    result = im.index(s)
    print(result)