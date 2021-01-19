def solution(n, lost, reserve):
    n -= len(lost)
    sm=[i for i in lost if i in reserve ]
    n+=len(sm)
    for lost_num in sm:
        reserve.remove(lost_num)
        lost.remove(lost_num)
    
    for lost_num in lost:
        if lost_num-1 in reserve:
            reserve.remove(lost_num-1)
            n+=1
        elif lost_num+1 in reserve:
            reserve.remove(lost_num+1)
            n+=1
    return n



if __name__ == '__main__':
    n, lost, reserve, expected=5,[2,4],[1,3,5],5
    print(f'-input\n n = {n}, lost ={lost}, reserve = {reserve}')
    print(f'-output\n expected : {expected}, result : {solution(n,lost,reserve)}')



