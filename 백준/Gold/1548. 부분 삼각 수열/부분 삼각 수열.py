N = int(input())
arry = list(map(int, input().split()))
arry.sort()
answer = 0

i = 0
j = i+1
k = len(arry)

if len(arry) >= 3:
    for i in range(len(arry) - 2):
        for j in range(i+1, len(arry) - 1):
            for k in range(j+1, len(arry)):
                if i == j or i == k or j == k:
                    continue
                
                if (arry[i] + arry[j]) > arry[k] and i < j:
                    # print((arry[i]+ arry[j]), arry[k])
                    # print(i, j, k, (k - j + 2))
                    if answer < (k - j + 2):
                        answer = k - j + 2
    if answer == 0:
        answer = 2
else:
    answer = len(arry)
                
print(answer)