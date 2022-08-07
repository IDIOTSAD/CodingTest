N = int(input())
data = list(map(int, input().split()))
answer = 0
arry = [1] * 1001

# make prime arry
for i in range(len(arry)):
    if i < 2:
        arry[i] = 0
        continue
    
    for j in range(i*i, len(arry), i):
        arry[j] = 0

for i in range(N):
    answer += arry[data[i]]
    
print(answer)