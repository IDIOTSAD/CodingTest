import sys, itertools

N = int(sys.stdin.readline())
arry = list(map(int, sys.stdin.readline().split()))
value = itertools.permutations(arry, N)
answer = 0

for val in value:
    ans = 0
    for i, v in enumerate(val):
        if i == len(val) - 1: break
        ans += abs(v - val[i+1])
    #print(val, ans)
    answer = max(answer, ans)
print(answer)