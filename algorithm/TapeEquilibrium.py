import math
#o(N)
def solution(A) :
    left = 0
    right = 0
    p = list(0 for i in range(0,len(A)-1))
    
    sum_ = 0
    
    for i in A:
        sum_+=i
    
    for i in range(len(A)-1):
        left = A[i]+left
        print(left)
        right = sum_- left
        print(right)
        p[i] = abs(left-right)
        
    return min(p)