#최소값 만들기

def solution(A,B):
    ans=[i*j for i,j in zip(sorted(A),sorted(B,reverse=True))]
    return sum(ans)

if __name__ == '__main__':
    a,b,e=[1,4,2],[5,4,4],29
    print(f'-input-\n A : {a}, B : {b}')
    print(f'-output-\n expected : {e}, result : {solution(a,b)}')

