#정수 삼각형
def solution(triangle):
    for i in triangle:
        g=len(i)
        d=[ii for ii in i]
        if len(i) <2:
            v=d
        else:
            for j,iv in enumerate(v):
                
                for k,p in enumerate(i[j:j+2]):

                    if (j+k ==0) or (j+k) ==g-1:
                        d[j+k]=iv+p
                    else:
                        d[j+k]=max(d[j+k],iv+p)
            v=d
    answer = max(v)
    return answer

if __name__ == '__main__':
    tri,expected=[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]], 30
    print(f'-input-\n triangle : {tri}')
    print(f'-output-\n expected : {expected}, result : {solution(tri)}')

