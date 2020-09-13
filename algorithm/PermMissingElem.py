def solution(A):
    A.sort() #o(nlogn)
    for i in range(0,len(A)-1): #len(A) = 4 ==> 0~3 => 0,1,2    #o(n)
        if A[i+1]-A[i] != 1 :
            return A[i]+1

    if A[len(A)-1] == len(A)+1 :
            return 1
    else :
            return len(A)+1 

solution(list([1]))
