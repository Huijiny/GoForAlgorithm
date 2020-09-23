def solution(A):
    #O(N)
    #(a,b)의 평균은 a보다 큼. (a,b,c,d)의 평균은 (a,b)보다 큼. 그래서 2,3개인거만 하면 돼.
    #실수 : 괄호...
    min_avg = (A[0]+A[1])/2
    min_idx = 0
    for i in range(2, len(A)):
        
        avg = (A[i-2]+A[i-1]+A[i])/3
        if min_avg > avg :
            min_avg = avg
            min_idx = i-2
        
        avg = (A[i-1]+A[i])/2
        if min_avg > avg :
            min_avg = avg
            min_idx = i-1

    return min_idx


print(solution([10, 10, -1, 2, 4, -1, 2, -1]))
