import sys

N = int(sys.stdin.readline())

for i in range(N):
    arry = list(sys.stdin.readline().strip())
    stack = []
    if arry[0] == ")":
        print("NO")
        continue
    
    stack.append(arry[0])
    
    for i in range(1, len(arry)):
        #print(stack)
        new = arry[i]
        if len(stack) > 0:
            curr = stack[-1]
            if new == ")" and curr == new:
                break
            elif new == ")" and curr != new:
                stack.pop()
            else:
                stack.append(new)
        else:
            stack.append(new)
    
    if len(stack) == 0: print("YES")
    else: print("NO")