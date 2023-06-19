from collections import deque

count = int(input())
stack_1 = deque(map(int, input().split()))
stack_2 = deque()
arry = []

while stack_1 or stack_2 or count:
    if stack_1:
        while stack_1:
            num = stack_1.pop()
            if num != count:
                stack_2.append(num)
                arry.append([1, 2])
            else:
                arry.append([1, 3])
                count -= 1
    else:
        while stack_2:
            num = stack_2.pop()
            if num != count:
                stack_1.append(num)
                arry.append([2, 1])
            else:
                arry.append([2, 3])
                count -= 1

print(len(arry))
for i in range(len(arry)):
    print(arry[i][0], arry[i][1])