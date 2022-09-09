from collections import deque
a = [1,2,3,4]
a = deque(a)
print(a[0])
a.rotate(1)
print(a[0])