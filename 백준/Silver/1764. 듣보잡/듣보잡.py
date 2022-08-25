import sys

N, M = map(int, sys.stdin.readline().split())
arry = {}
result = {}

for i in range(N):
    arry[sys.stdin.readline().strip()] = i
for j in range(M):
    word = sys.stdin.readline().strip()
    #print(word, arry, result) 
    if word in arry.keys():
        result[j] = word

print(len(result))
result = sorted(result.items(), key= lambda item: item[1])
for re in result:
    print(re[1])
