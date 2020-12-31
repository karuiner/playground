#H-index
def solution(citations):
    ans=0
    n=len(citations)
    for i in range(n,0,-1):
        j,k=0,0
        for p in citations:
            if p >= i:
                j+=1
            else:
                k+=1
        if (j >=i) and (k <i):
            ans= i
            break
    return ans

if __name__ == '__main__':
    c,e=[3,0,6,1,5],3
    print(f'-input-\n citation : {c}')
    print(f'-output-\n expected : {e}, result : {solution(c)}')

