import heapq

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
result = [0] * (N+1)

for i in range(M):
    start, end, value = map(int, input().split())
    graph[start].append((end, value))

def dijkstra(start):
    q = []
    # 초기 설정
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
for i in range(1, N+1):
    distance = [999999] * (N+1)
    dijkstra(i)
    if distance[i] == 999999:
        print("INFINITY")
    else:
        result[i] += distance[X]
    
    distance = [999999] * (N+1)
    dijkstra(X)
    
    if distance[i] == 999999:
        print("INFINITY")
    else:
        result[i] += distance[i]
    
print(max(result))