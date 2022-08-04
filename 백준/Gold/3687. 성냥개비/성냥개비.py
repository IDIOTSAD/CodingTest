N = int(input())
#            0123456789
num_match = '6255456376'
temp = [2, 3, 4, 5, 6, 7]
r_temp = [7, 6, 5, 4, 3, 2]
d = [0, 0, 1, 7, 4, 2, 6, 8, 10, 18, 22]

for _ in range(N):
    num = int(input())
    max_num = []
    min_num = []
    num1 = num
    
    if num < 11:
        min_num.append(d[num])
    else:
        min_num = [8 for i in range((num+6)//7)]
        if  num % 7 ==1: min_num[0]=1; min_num[1]=0
        if  num % 7 ==2: min_num[0]=1
        if  num % 7 ==3: min_num[0]=2; min_num[1]=0; min_num[2]=0
        if  num % 7 ==4: min_num[0]=2; min_num[1]=0
        if  num % 7 ==5: min_num[0]=2
        if  num % 7 ==6: min_num[0]=6
    
    for t in temp:
        while ((num1 - t) > 1 or num1 == t):
            num1 = num1 - t
            max_num.append(str(num_match.rfind(str(t))))
    
    max_num.reverse()

    print(''.join(map(str, min_num)) + ' ' + ''.join(max_num))