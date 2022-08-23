from collections import deque
subin_pos, bro_pos = map(int, input().split())
is_visit = [False] * (100001)
queue = deque()
queue.append([subin_pos, 0])
is_visit[subin_pos] = True

def get_time():
    move = [-1, 1, 0]
    teleport = [1, 1, 2]
    while queue:
        now_pos, time = queue.popleft()
        if now_pos == bro_pos:
            return time
        for i in range(len(move)):
            new_pos = (now_pos + move[i]) * teleport[i]
            if 0 <= new_pos <= 100000 and is_visit[new_pos] == False:
                queue.append([new_pos, time+1])
                is_visit[new_pos] = True

result = get_time()

print(result)