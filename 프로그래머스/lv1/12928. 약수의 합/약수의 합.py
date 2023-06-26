import math

def solution(n):
    answer = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if (n % i == 0 and n // i == i): answer += i
        elif (n % i == 0): answer += (n / i) + i
    
    return answer