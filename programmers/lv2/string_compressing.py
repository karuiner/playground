#문자열 압축
def solution(s):
    n=len(s)
    ans = 0
    for j in range(1,len(s)+1):
        k=[s[i:i+j] for i in range(0,len(s),j) ]
        
        p=''
        c=0
        for i,y in enumerate(k):
            if not i:
                c+=1
                u=y
            else:
                if y == u:
                    c+=1
                else:
                    if c <2:
                        p+=u
                        c=1
                        u=y
                    else:
                        p+=f'{c}{u}'
                        c=1
                        u=y                        
        if c<2:
            p+=u 
        else:            
            p+=f'{c}{u}'
        if j ==1:
            ans=len(p)
        else:
            ans=min(len(p),ans)    
    return ans

if __name__ == '__main__':
    s,e="aabbaccc",7
    print(f'-input-\n string : {s}')
    print(f'-output-\n expected : {e}, result : {solution(s)}')
