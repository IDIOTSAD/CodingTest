from itertools import combinations

r = int(input())

axis_x = [0, 1, 0, -1, 0]
axis_y = [0, 0, 1, 0, -1]

arry = []
value = {}
answer = 99999999

for i in range(r):
    cols = list(map(int, input().split()))
    arry.append(cols)

for i in range(1, r-1):
    for j in range(1, r-1):
        sum = 0
        for k in range(len(axis_x)):
            sum += arry[i + axis_x[k]][j + axis_y[k]]
            #print(i, j, arry[i + axis_x[k]][j + axis_y[k]], sum)
        value[(i, j)] = sum

for comb in combinations(value, 3):
    for com in combinations(comb, 2):
        if abs(com[0][0] - com[1][0]) + abs(com[0][1] - com[1][1]) <= 2:
            break
    else:
        sum = 0
        for com in comb:
            sum += value[com]
        answer = min(answer, sum)

print(answer)