num = int(input())
arry = dict()

for i in range(num):
    a, b = map(int, input().split())
    for i in range(a, b+1):
        if i in arry:
            arry[i] += 1
        else:
            arry[i] = 1

arry = sorted(arry.items())

total = 0
w = 0
h = 0
prev = 0
for key, value in list(arry):
    # init h, w
    if w == 0 and h == 0:
        prev = key
        w = 1
        h = value
    else:
        if (prev + 1) != key:
            total += w * h
            prev = key
            w = 1
            h = value
        else:
            prev = key
            w += 1
            if h < value:
                h = value
    '''
    print('======')
    print(key, value)
    print(total, w, h)
    print('======')
    '''
total += w * h
print(total)