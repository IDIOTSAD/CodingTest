import sys

N = int(sys.stdin.readline())
arry = []
for i in range(N):
    arry.append(int(sys.stdin.readline()))
    
arry.sort()

for i in range(N):
    print(arry[i])