def solution(A):
    count_0 = 0
    cars = 0
    for idx, n in enumerate(A):
        if n == 0 : 
            count_0 += 1
        elif n == 1:
            cars += (count_0*1)
    
    if cars > 1000000000 :
        return -1
    else :
        return cars
    
print(solution([0,1,0,1,1]))