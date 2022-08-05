from itertools import combinations

N = int(input())
S_arry = []
B_arry = []
min = 9999999999

for _ in range(N):
    S, B = map(int, input().split())
    S_arry.append(S)
    B_arry.append(B)
    
for i in range(1, N+1):
    combination = list(combinations([i for i in range(len(S_arry))], i))
    for comb in combination:
        S_sum = 1
        B_sum = 0
        for com in comb:
            S_sum *= S_arry[com]
            B_sum += B_arry[com]
        #print(comb, S_sum, B_sum, B_arry[com])
        if abs(S_sum - B_sum) < min:
            min = abs(S_sum - B_sum)
        
print(min)
        