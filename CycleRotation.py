def solution(A, K):
    l = len(A) #4
    for _ in range(K):
        B = list(0 for i in range(l))
        for i, num in enumerate(A):
            B[i+1-l] = num # 3+1-len(A)
        A = B    
    
return A