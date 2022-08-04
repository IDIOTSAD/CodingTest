import copy

N, M = map(int, input().split())
arry = []
result = []

for i in range(N):
    arry.append(list(input()))

for i in range(N-8 + 1):
    for j in range(M-8 + 1):
        lu = copy.deepcopy(arry[i][j])
        ru = copy.deepcopy(arry[i][j + 7])
        ld = copy.deepcopy(arry[i + 7][j])
        rd = copy.deepcopy(arry[i + 7][j + 7])
        lu_cnt, ru_cnt, ld_cnt, rd_cnt = 0, 0, 0, 0
        for c in range(1, 9):
            for k in range(8 - c + 1):
                if k == 0:
                    if arry[i+(c-1)][j+(c-1)+k] != lu: lu_cnt += 1
                    if arry[i+(c-1)][j+7-(c-1)-k] != ru: ru_cnt += 1
                    if arry[i+7-(c-1)-k][j+(c-1)] != ld: ld_cnt += 1
                    if arry[i+7-(c-1)-k][j+7-(c-1)] != rd: rd_cnt += 1
                elif k % 2 == 0:
                    if arry[i+(c-1)][j+(c-1)+k] != lu: lu_cnt += 1
                    if arry[i+(c-1)+k][j+(c-1)] != lu: lu_cnt += 1
                    if arry[i+(c-1)][j+7-(c-1)-k] != ru: ru_cnt += 1
                    if arry[i+(c-1)+k][j+7-(c-1)] != ru: ru_cnt += 1
                    if arry[i+7-(c-1)-k][j+(c-1)] != ld: ld_cnt += 1
                    if arry[i+7-(c-1)][j+(c-1)+k] != ld: ld_cnt += 1
                    if arry[i+7-(c-1)-k][j+7-(c-1)] != rd: rd_cnt += 1
                    if arry[i+7-(c-1)][j+7-(c-1)-k] != rd: rd_cnt += 1
                else:
                    if arry[i+(c-1)][j+(c-1)+k] == lu: lu_cnt += 1
                    if arry[i+(c-1)+k][j+(c-1)] == lu: lu_cnt += 1
                    if arry[i+(c-1)][j+7-(c-1)-k] == ru: ru_cnt += 1
                    if arry[i+(c-1)+k][j+7-(c-1)] == ru: ru_cnt += 1
                    if arry[i+7-(c-1)-k][j+(c-1)] == ld: ld_cnt += 1
                    if arry[i+7-(c-1)][j+(c-1)+k] == ld: ld_cnt += 1
                    if arry[i+7-(c-1)-k][j+7-(c-1)] == rd: rd_cnt += 1
                    if arry[i+7-(c-1)][j+7-(c-1)-k] == rd: rd_cnt += 1
        #print(lu_cnt, ru_cnt, ld_cnt, rd_cnt)
        result.append(min(lu_cnt, ru_cnt, ld_cnt, rd_cnt))
        if lu == 'B': lu = 'W'
        else: lu = 'B'
        if ru == 'B': ru = 'W'
        else: ru = 'B'
        if ld == 'B': ld = 'W'
        else: lu = 'B'
        if rd == 'B': rd = 'W'
        else: rd = 'B'
        lu_cnt, ru_cnt, ld_cnt, rd_cnt = 0, 0, 0, 0
        for c in range(1, 9):
            for k in range(8 - c + 1):
                if k == 0:
                    #print(c-1, k)
                    #print(lu, ru, ld, rd)
                    #print(arry[i+(c-1)][j+(c-1)], arry[i+(c-1)][j+7-(c-1)], arry[i+7-(c-1)][j+(c-1)], arry[i+7-(c-1)][j+7-(c-1)])
                    #print(lu_cnt, ru_cnt, ld_cnt, rd_cnt)
                    if arry[i+(c-1)][j+(c-1)+k] != lu: lu_cnt += 1; #print(i+(c-1), j+(c-1)+k)
                    if arry[i+(c-1)][j+7-(c-1)-k] != ru: ru_cnt += 1
                    if arry[i+7-(c-1)-k][j+(c-1)] != ld: ld_cnt += 1
                    if arry[i+7-(c-1)-k][j+7-(c-1)] != rd: rd_cnt += 1
                    
                elif k % 2 == 0:
                    #print(c-1, k)
                    #print(lu, ru, ld, rd)
                    #print(arry[i+(c-1)][j+(c-1)], arry[i+(c-1)][j+7-(c-1)], arry[i+7-(c-1)][j+(c-1)], arry[i+7-(c-1)][j+7-(c-1)])
                    #print(lu_cnt, ru_cnt, ld_cnt, rd_cnt)
                    if arry[i+(c-1)][j+(c-1)+k] != lu: lu_cnt += 1; #print(i+(c-1), j+(c-1)+k)
                    if arry[i+(c-1)+k][j+(c-1)] != lu: lu_cnt += 1; #print(i+k+(c-1), j+(c-1))
                    if arry[i+(c-1)][j+7-(c-1)-k] != ru: ru_cnt += 1
                    if arry[i+(c-1)+k][j+7-(c-1)] != ru: ru_cnt += 1
                    if arry[i+7-(c-1)-k][j+(c-1)] != ld: ld_cnt += 1
                    if arry[i+7-(c-1)][j+(c-1)+k] != ld: ld_cnt += 1
                    if arry[i+7-(c-1)-k][j+7-(c-1)] != rd: rd_cnt += 1
                    if arry[i+7-(c-1)][j+7-(c-1)-k] != rd: rd_cnt += 1
                else:
                    #print(c-1, k)
                    #print(lu, ru, ld, rd)
                    #print(arry[i+(c-1)][j+(c-1)], arry[i+(c-1)][j-(c-1)], arry[i-(c-1)][j+(c-1)], arry[i-(c-1)][j-(c-1)])
                    #print(lu_cnt, ru_cnt, ld_cnt, rd_cnt)
                    if arry[i+(c-1)][j+(c-1)+k] == lu: lu_cnt += 1; #print(i+(c-1), j+(c-1)+k)
                    if arry[i+(c-1)+k][j+(c-1)] == lu: lu_cnt += 1; #print(i+k+(c-1), j+(c-1))
                    if arry[i+(c-1)][j+7-(c-1)-k] == ru: ru_cnt += 1
                    if arry[i+(c-1)+k][j+7-(c-1)] == ru: ru_cnt += 1
                    if arry[i+7-(c-1)-k][j+(c-1)] == ld: ld_cnt += 1
                    if arry[i+7-(c-1)][j+(c-1)+k] == ld: ld_cnt += 1
                    if arry[i+7-(c-1)-k][j+7-(c-1)] == rd: rd_cnt += 1
                    if arry[i+7-(c-1)][j+7-(c-1)-k] == rd: rd_cnt += 1
        #print(lu_cnt, ru_cnt, ld_cnt, rd_cnt)
        result.append(min(lu_cnt, ru_cnt, ld_cnt, rd_cnt))

print(min(result))