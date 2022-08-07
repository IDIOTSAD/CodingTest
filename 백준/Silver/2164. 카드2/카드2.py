from collections import deque

N = int(input())
arry = deque()

for i in range(N, 0, -1):
    arry.append(i)

while len(arry) > 1:
    arry.pop()
    arry.appendleft(arry[-1])
    arry.pop()

print(arry[0])