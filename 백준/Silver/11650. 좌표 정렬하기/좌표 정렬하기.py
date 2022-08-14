import sys

N = int(sys.stdin.readline())
arry = []

for _ in range(N):
    arry.append(list(map(int, sys.stdin.readline().split())))

arry.sort(key=lambda x: x[1])
arry.sort(key=lambda x: x[0])

for x, y in arry:
    print(str(x) + " " +  str(y))