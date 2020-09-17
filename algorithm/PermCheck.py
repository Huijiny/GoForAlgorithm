def solution(A) :
    A.sort()
    tmp = 1

    for num in A:
        if num == tmp :
            tmp+=1
        else:
            return 0
    return 1
    

print(solution([1000,1]))