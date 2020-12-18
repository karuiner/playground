#모의고사
def solution(answers):
    n=len(answers)
    b1=[1,3,4,5]
    c1=[3,1,2,4,5]
    a=[ (i%5)+1 for i in range(n)]
    b=[ 2 if (i+1)%2 else b1[(i//2)%4] for i in range(n)  ]
    c=[c1[(i//2)%5]  for i in range(n) ]
    db={}
    su=[1,2,3]
    for i in su:
        db[i]=0
    for i, v in enumerate(answers):
        if v == a[i]:
            db[su[0]]+=1
        if v == b[i]:
            db[su[1]]+=1
        if v == c[i]:
            db[su[2]]+=1
    k=[i for i in db.values()]
    ans=[su[i] for i,ik in enumerate(k)  if max(k) == ik]
        
    
    return ans

if __name__ == '__main__':
    a=[1,2,3,4,5]
    expected=[1]
    print(f'input : {a}')
    print(f'expected : {expected}, result : {solution(a)}')

