#소수 찾기
import itertools
import math

def solution(numbers):
    n=list(numbers)
    np=[]
    for i in range(1,len(n)+1):
        p=list(map(''.join, itertools.permutations(n,i)))
        np+=p
    k=list(map(int,np))
    sp=set(k)
    prime=[2,3,5]
    def check(n):
        if n < 2:
            return False
        sq=math.sqrt(n)
        z=range(2,int(sq)+1)
        m=1
        for i in z:
            if not n%i:
                m=0
            
        if m:
        	return True
        else:
            return False
        
        
    return sum(list(map(check,sp)))

if __name__ == '__main__':
    n,expected="17",3
    print(f'-input-\n  number : {n}')
    print(f'-output-\n expected : {expected}, result : {solution(n)}')


