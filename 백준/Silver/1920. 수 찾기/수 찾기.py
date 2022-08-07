N = int(input())
arry = list(map(int, input().split()))
arry = dict.fromkeys(arry, 0)
M = int(input())
data = list(map(int, input().split()))

for i in range(M):
    if data[i] in arry:
        print(1)
    else:
        print(0)