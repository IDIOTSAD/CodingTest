import sys

N, r, c = map(int, sys.stdin.readline().split())


def divide(N, i, j, start, end):
    cal = end % (pow(2, N-1) * pow(2, N-1))
    #print(N, i, j, start, end, cal, (pow(2, N-1) * pow(2, N-1)))
    if r == i and c == j:
        print(end)
        return
    
    if r <= i - pow(2, N-1) and c <= j - pow(2, N-1):
        divide(N-1, i - pow(2, N-1), j - pow(2, N-1), start, start + cal)
    elif r <= i - pow(2, N-1) and c <= j:
        divide(N-1, i - pow(2, N-1), j, start + cal + 1, start + cal * 2 + 1)
    elif r <= i and c <= j - pow(2, N-1):
        divide(N-1, i, j - pow(2, N-1), start + cal * 2 + 2, start + cal * 3 + 2)
    else:
        divide(N-1, i, j, start + cal * 3 + 3, start + cal * 4 + 3)
    
divide(N, (pow(2, N) - 1), pow(2, N) - 1, 0, pow(2, N) * pow(2, N) - 1)
