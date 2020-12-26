# 124나라의 숫자

def solution(n):
    d=""
    while( n ):
        n,b=divmod(n,3)
        d="412"[b]+d
        if not b:
            n-=1
    
    return d

if __name__ == '__main__':
    n=[1,2,3,4,5,6,7,8,9,10]
    print('input  output')
    for i in n:
        print(f'{i:>5}  {solution(i):>6}')
