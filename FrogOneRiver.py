def solution(X, A):
    time = [0 for _ in range(X)]
    match = 0
    yon = [False for _ in range(X)]
    # write your code in Python 3.6
    for i, num in enumerate(A):
        if yon[num-1] == False :
            yon[num-1] = True
            time[num-1] = i
            match += 1
            print(match)
            if match == X:
                print(match)
                return max(time)
    return -1

print(solution(5,[1, 3, 1, 4, 2, 3, 5, 4]))
        
        