import sys

N = int(sys.stdin.readline())
arry = []
money = []

for i in range(N):
    dic = {}
    temp = list(map(int, sys.stdin.readline().split()))
    for t in temp:
        if t not in dic.keys():
            dic[t] = 1
        else:
            dic[t] += 1
    dic = sorted(dic.items(), key=lambda x: (-x[1], -x[0]))
    arry.append(dic)

for arr in arry:
    if arr[0][1] == 3:
        money.append(10000 + arr[0][0] * 1000)
    elif arr[0][1] == 2:
        money.append(1000 + arr[0][0] * 100)
    else:
        money.append(arr[0][0] * 100)
print(max(money))
