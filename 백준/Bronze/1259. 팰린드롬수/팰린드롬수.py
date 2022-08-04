while True:
    num = list(input())
    
    if num[0] == '0':
        break
    
    start = 0
    end = (len(num) - 1)
    
        
    while start <= end:
        if len(num) == 1:
            print("yes")
            break
        
        if num[start] != num[end]:
            print("no")
            break
        else:
            start += 1
            end -= 1
            
        if start >= end:
            print("yes")
            break