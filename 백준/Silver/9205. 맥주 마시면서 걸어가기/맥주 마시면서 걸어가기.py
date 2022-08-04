test_case = int(input())

for _ in range(test_case):
    conv = int(input())
    distance = [[99] * (conv + 2) for i in range(conv + 2)]
    arry = []
    for i in range(conv + 2):
        arry.append(list(map(int, input().split())))
    
    for i in range(conv + 2):
        for j in range(conv + 2):
            if i == j:
                continue
            manhatan = abs(arry[i][0] - arry[j][0]) + abs(arry[i][1] - arry[j][1])

            if manhatan <= 1000:
                distance[i][j] = 1
    
    for k in range(conv + 2):
        for i in range(conv + 2):
            for j in range(conv +2):
                if distance[i][k] == 1 and distance[k][j] == 1:
                    distance[i][j] = 1
    
    if 0 <= distance[0][conv + 1] <= 98:
        print('happy')
    else:
        print('sad')