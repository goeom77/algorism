# 선택정렬 함수를 재귀적 알고리즘 작성
def SelectionSort(A,a):
    n = len(A)
    for i in range(a+1,n):
        if A[a] > A[i]:
            A[a],A[i] = A[i],A[a]
    if a+1 == n-1:
        return
    else:
        return SelectionSort(A,a+1)



A = [2,4,6,1,9,8,7,0]
SelectionSort(A,0)
print(A)