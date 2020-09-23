def solution(S, P, Q) :
    
    impact = list(['A','C','G','T'])
    result = list([])

    for i, num in enumerate(P) :
        if impact.index(S[num]) > impact.index(S[Q[i]]) :
            result.append(impact.index(S[Q[i]])+1)
        else :
            result.append(impact.index(S[num])+1)
    return result
print(solution("CCCCCCC",[1,5,0],[2,6,6]))