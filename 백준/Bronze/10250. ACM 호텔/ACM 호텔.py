import sys

T = int(sys.stdin.readline())

def acm(H, W, N):
    count = 1
    for i in range(1, W+1):
        for j in range(1, H+1):
            if count == N:
                print(str(j)+str(i).zfill(2))
                return
            count += 1
for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    acm(H, W, N)