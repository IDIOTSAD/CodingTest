import sys
from collections import deque

N = list(map(int, sys.stdin.readline().split()))
Q = list(map(int, sys.stdin.readline().split()))
L = deque()
T = deque()
answer = 0
Q.reverse()

while Q or L:
    #print(Q, L, T)
    if T and T[0] == 0:
        T.popleft()
        L.popleft()
    if Q and sum(L) + Q[-1] <= N[2]:
        L.append(Q[-1])
        T.append(N[1])
        Q.pop()
    for i in range(len(T)):
        T[i] -= 1
    answer += 1
print(answer)