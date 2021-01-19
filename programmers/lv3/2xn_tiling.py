#2xn 타일링
def solution(n):
        
    ap=[]
    ap.append(0)
    ap.append(1)
    ap.append(2)
    ap.append(3)
    for i in range(4,n+1):
        lp=(ap[i-1]+ap[i-2])%1000000007
        ap.append(lp)
        
    return ap[n]

if __name__ == '__main__':
    n,expected=4,5
    print(f'-input-\n n : {n}')
    print(f'-output-\n expected : {expected}, result : {solution(n)}')
