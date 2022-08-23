import sys

N = int(sys.stdin.readline())
arry = [0] * 1000001

for i in range(2, N+1):
    arry[i] = arry[i-1] + 1
    if i % 2 == 0:
        arry[i] = min(arry[i], arry[i // 2] + 1)
    if i % 3 == 0:
        arry[i] = min(arry[i], arry[i // 3] + 1)
    
print(arry[N])