import heapq
import sys

N = int(sys.stdin.readline())
heap = []

for i in range(N):
    num = int(sys.stdin.readline())
    if num == 0 and len(heap) == 0:
        print(0)
    elif num == 0:
        print(heap[0])
        heapq.heappop(heap)
    else:
        heapq.heappush(heap, num)