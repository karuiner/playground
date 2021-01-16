#점프와 순간이동
def solution(n):    
    def f(x,y):
        if x == 1 : return y+1
        return f((x-1)//2,y+1) if x%2 else f(x//2,y)
    return f(n,0)


if __name__ == '__main__':
    n,e=5000,5
    print(f'-input-\n N : {n}')
    print(f'-output-\n expected : {e}, result : {solution(n)}')


