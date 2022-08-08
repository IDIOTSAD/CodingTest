import sys

while True:
    arry = list(map(int, sys.stdin.readline().split()))
    if sum(arry) == 0: break
    
    arry.sort()
    if pow(arry[0], 2) + pow(arry[1], 2) == pow(arry[2], 2): print("right")
    else: print("wrong")
    