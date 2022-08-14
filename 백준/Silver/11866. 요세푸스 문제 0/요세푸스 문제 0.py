import sys

N, K = map(int, sys.stdin.readline().split())
arry = []
result = []

for i in range(1, N+1):
    arry.append(i)
    
prev = 0
for i in range(N):
    result.append(str(arry[(prev + K - 1) % len(arry)]))
    del arry[(prev + K - 1) % len(arry)]
    prev = (prev + K - 1) % (len(arry) + 1)
    
print("<" + ", ".join(result) + ">")