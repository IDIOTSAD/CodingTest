import sys

aeiou = ['a', 'e', 'i', 'o', 'u']
words = []

def dfs(idx, index, visit, depth, max_depth):
    global words
    depth += 1
    if depth == max_depth:
        cnt = 0
        temp = ""
        for i, vi in enumerate(visit):
            if vi == 1: temp += str(index[i])
        for a in aeiou:
            cnt += temp.count(a)
        if cnt >= 1 and max_depth - cnt > 1:
            words.append(temp)
            #print("curr value = ", temp, visit, index)
        return
    else:
        for i in range(idx, len(index)):
            if visit[i] == 0 and i > idx and depth < max_depth:
                visit[i] = 1
                dfs(i, index, visit, depth, max_depth)
                visit[i] = 0

N = list(map(int, sys.stdin.readline().split()))
visit = [0 for i in range(N[1])]
word = list(map(str, sys.stdin.readline().split()))
word.sort()

for idx, wor in enumerate(word):
    if len(word) - idx >= N[0]:
        visit[idx] = 1
        dfs(idx, word, visit, 0, N[0])
        visit[idx] = -1
    else: break

for w in words:
    print(w)