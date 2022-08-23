import sys

N, M = map(int, sys.stdin.readline().split())

dict = {}
dict2 = {}

for i in range(1, N+1):
    poketmon = sys.stdin.readline().strip()
    dict[i] = poketmon
    dict2[poketmon] = i

for j in range(M):
    search = sys.stdin.readline().strip()
    
    if search.isdigit():
        print(dict.get(int(search)))
    else:
        print(dict2.get(search))