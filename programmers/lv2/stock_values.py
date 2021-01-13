#주식 가격
def solution(prices):
    n=len(prices)
    a=[0]*n
    for i,v in enumerate(prices[:-1]):
        k=i
        ck= True
        while ck: 
            if prices[k] >= v:
                k+=1
            else:
                ck=False
            if k > n-2:
                ck= False
        a[i]=k-i
            
    answer = a
    return answer


if __name__ == '__main__':
    p,expected=[1, 2, 3, 2, 3], [4, 3, 1, 1, 0]
    print(f'-input-\n  prices : {p}')
    print(f'-output-\n expected : {expected}, result : {solution(p)}')


