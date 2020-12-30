#삼각달팽이
def solution(n):
    sn=sum([i for i in range(1,n+1)])
    p=[[0 for j in range(i)] for i in range(1,n+1)]
    ph=1
    i,j=0,0
    def f(p,i,j,ph):
        if ph ==1:
            p[i][j]=k
            if i+1 <= n-1 and p[i+1][j] == 0:
                i+=1
            else:
                ph+=1
                j+=1
        elif ph ==2:
            p[i][j]=k
            if j+1 <= n-1 and p[i][j+1] == 0:
                j+=1
            else:
                ph+=1
                i-=1
                j-=1
        else:
            p[i][j]=k
            if ((i-1 >= 0) and(j-1>=0)) and p[i-1][j-1] == 0:
                i-=1
                j-=1
            else:
                ph=1
                i+=1
        return p,i,j,ph
    for k in range(1,sn+1):
        try:
            p,i,j,ph=f(p,i,j,ph)
        except:
            break
            
    answer = sum(p,[])
    return answer

if __name__ == '__main__':
    n,expected=4,[1,2,9,3,10,8,4,5,6,7]
    print(f'-input-\n n : {n}')
    print(f'-output-\n expected : {expected}, result : {solution(n)}')


