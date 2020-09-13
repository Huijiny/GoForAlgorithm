def solution(N) :
    n = str(getBinary(N))
    start = False
    count = 0
    maxVal = 0

    for num in n:
        if num == '1' :
            if start == False : #맨 첫번째 시작만 start로 바꿔주는 애. 트리거.
                start = True
            else : #그 다음부터 start는 계속 true일테니까 그 다음부터 1만나면 계속 여기로 와서 max count 처리 해줘.
                if count>maxVal : 
                    maxVal = count
                count = 0
        
        if start and num == '0':
            count+=1
    print(maxVal)

def getBinary(N):
    n = ''
    while N>0:
        n = str(N%2)+n
        N = N//2
    return n
solution(529)