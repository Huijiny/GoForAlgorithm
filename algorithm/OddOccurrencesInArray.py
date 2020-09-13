
def solution(A):
    # write your code in Python 3.6
    A.sort()
    while(len(A) != 0):
        if len(A) != 1:#마지막 애가 아니면 다음것과 비교.
            if A[0] == A[1]:# 같으면 슬라이싱
                A = A[2:]
            else: #다르면 num
                return A[0]
        else: #마지막 번호라면 얘가 짝이 없는애.
            return A[0]
