import sys

def solution(A) :

    if max(A)<1 :
        return 1
    else :
        A = sorted(set([a for a in A if a > 0]))

        for idx, num in enumerate(A,1):
            if idx != num :
                return idx 
        return A[-1]+1

        
print(solution([-1,-2,3]))