N = int(input())
arry = []
for i in range(N):
    word = input()
    if not word in arry:
        arry.append(word)

arry.sort()
arry.sort(key=lambda x : len(x))

for arr in arry:
    print(arr)