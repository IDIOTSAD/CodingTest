count = int(input())
arry = list(map(int, input().split()))
arry.sort()
result = 0
for i in range(count):
    target = arry[i]
    left, right = 0, len(arry)-1
    while left < right:
        tmp = arry[left] + arry[right]
        if tmp > target or right == i: 
            right -= 1
        elif tmp < target or left == i:
            left += 1
        else:
            result += 1
            break

print(result)