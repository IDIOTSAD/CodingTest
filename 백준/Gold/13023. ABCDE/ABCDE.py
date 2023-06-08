import sys
sys.setrecursionlimit(10**6)

def dfs(cur, s, vis, d):
    global answer
    if d >= 5:
        answer = 1
        return
    vis[cur] = 1
    for i in s[cur]:
        if vis[i] == 0:
            vis[i] = 1
            dfs(i, s, vis, d+1)
            vis[i] = 0
    vis[cur] = 0

N = list(map(int, sys.stdin.readline().split()))
sour = [ [] for i in range(N[0]) ]
visit = [ 0 for i in range(N[0]) ]
answer = 0

for i in range(N[1]):
    value = list(map(int, sys.stdin.readline().split()))
    sour[value[0]].append(value[1])
    sour[value[1]].append(value[0])
    
for i in range(N[0]):
    visit[i] = 1
    depth = 1
    dfs(i, sour, visit, depth)
    visit[i] = 0
    if answer: break

print(answer)