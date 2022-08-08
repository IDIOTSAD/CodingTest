import sys

N = int(sys.stdin.readline())
arry = []

for i in range(N):
    age, name = sys.stdin.readline().split()
    arry.append([age, name, i])
    
arry.sort(key=lambda x : (int(x[0]), int(x[2])))

for i in range(N):
    print(arry[i][0] + ' ' + arry[i][1])