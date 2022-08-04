from collections import deque
from copy import deepcopy
import time

def bfs():
    while q:
        x, y, d = q.popleft()
        #print(x, y, d)
        wall = deepcopy(arry)
        # if dead?
        
        # update wall
        for _ in range(d):
            wall.pop()
            
        if d >= 8 or x >= len(wall):
            #print('dead')
            continue
        
        #show = deepcopy(wall)
        #show[x][y] = '%'
        #for i in range(len(show)):
        #    print(show[i])
        #print()
        #time.sleep(0.2)
        
        # if end?
        if x == 0:
            return 1
        
        # axis check
        for joy_x, joy_y in zip(axis_x, axis_y):
            new_x = x + joy_x
            new_y = y + joy_y
            
            if 0 <= new_x < len(wall) and 0 <= new_y < len(wall[0]) and wall[new_x][new_y] != '#':
                if (new_x - 1 >= 0) and wall[new_x -1][new_y] != '#':
                    #print("select = ", joy_x, joy_y, new_x, new_y)
                    q.appendleft([new_x - 1, new_y, d+1])
                elif new_x == 0 and wall[new_x][new_y] != '#':
                    q.appendleft([new_x, new_y, d+1])
    return 0

arry = []
axis_x = [-1, -1, -1, 1, 1, 1, 0, 0, 0, 0]
axis_y = [-1, 0, 1, 1, 0, -1, 0, 1, -1, 0]
#arry.append(list('........'))

#input list
for _ in range(8):
    rows = list(input())
    arry.append(rows)
    
q = deque()
q.appendleft([7, 0, 0])
answer = bfs()

print(answer)