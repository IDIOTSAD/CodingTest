import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
instructor = ["push_front", "push_back", "pop_front", "pop_back", "size", "empty", "front", "back"]
stack = deque()

for i in range(N):
    inst = list(sys.stdin.readline().rstrip().split())
    if inst[0] == instructor[0]:
        stack.appendleft(inst[1])
    elif inst[0] == instructor[1]:
        stack.append(inst[1])
    elif inst[0] == instructor[2]:
        if stack: print(stack[0]); stack.popleft()
        else: print(-1)
    elif inst[0] == instructor[3]:
        if stack: print(stack[-1]); stack.pop()
        else: print(-1)
        
    elif inst[0] == instructor[4]:
        print(len(stack))
    elif inst[0] == instructor[5]:
        if stack: print(0)
        else: print(1)
    elif inst[0] == instructor[6]:
        if stack: print(stack[0])
        else: print(-1)
    elif inst[0] == instructor[7]:
        if stack: print(stack[-1])
        else: print(-1)
        