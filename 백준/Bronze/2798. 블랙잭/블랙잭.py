import sys

N, M = map(int, sys.stdin.readline().split())
arry = list(map(int, sys.stdin.readline().split()))

def check(arry):
    similar = 0
    for i in range(len(arry) - 2):
        for j in range(i+1, len(arry) - 1):
            for k in range(j+1, len(arry)):
                sum = arry[i] + arry[j] + arry[k]
                
                if sum == M: return sum
                
                if abs(M - sum) < abs(M - similar) and sum < M:
                    similar = sum
    return similar
            
result = check(arry)
print(result)