def solution(A,B,K):
    
    if A == 0 :
        return (B // K) +1
    else :
        return (B // K) - ((A - 1) // K) 

print(solution(6,11,2))