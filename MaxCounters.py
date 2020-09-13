
def solution(N, A):
    timer = [0 for _ in range(N)]
    max_ = 0
    tmp = 0
    for i, num in enumerate(A):
        if 1 <= num < N+1 : 
            idx = num-1
            
            if timer[idx]< max_:
                timer[idx] = max_

            timer[idx] += 1

            if tmp + max_ < timer[idx]: #이 줄 잘 이해안감.
                tmp = timer[idx]-max_

        elif num == N+1 :
           max_ += tmp
           tmp = 0
    for i in range(len(timer)):
        if timer[i] < max_:
            timer[i] = max_
    return timer

print(solution(5,[3,4,4,6,1,4,4]))