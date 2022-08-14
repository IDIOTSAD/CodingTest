import sys

N = int(sys.stdin.readline().rstrip())
instructor = ["push", "pop", "size", "empty", "top"]
stack = []

for i in range(N):
    inst = list(sys.stdin.readline().rstrip().split())
    if inst[0] == instructor[0]:
        stack.append(inst[1])
    elif inst[0] == instructor[1]:
        if stack: print(stack[-1]); stack.pop()
        else: print(-1)
    elif inst[0] == instructor[2]:
        print(len(stack))
    elif inst[0] == instructor[3]:
        if stack: print(0)
        else: print(1)
    elif inst[0] == instructor[4]:
        if stack: print(stack[-1])
        else: print(-1)