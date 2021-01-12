#뉴스 클러스터링
def solution(str1, str2):
    a=[ str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalnum()*str1[i].isalpha()*str1[i+1].isalpha()  ]
    b=[ str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalnum()*str2[i].isalpha()*str2[i+1].isalpha() ]
    if (len(a) != len(set(a))) or (len(b) != len(set(b))):
        c,d={},{}
        def da(b):
            a={}
            for i in b:
                if not i in a:
                    a[i]=1
                else:
                    a[i]+=1
            return a        
        ci=da(a)
        di=da(b)       
        e,f=set(a) & set(b),set(a) | set(b)
        c,d=0,0
        for i in e:
            p=0
            if i in ci:
                p=ci[i]
            if i in di:
                p=min(p,di[i])
            c+=p
            
        for i in f:
            p=0
            if i in ci:
                p=ci[i]
            if i in di:
                p=max(p,di[i])
            d+=p 
    else:
        c,d=len(set(a) & set(b)),len(set(a) | set(b))
    if d ==0:
        ans=1
    else:
        ans=c/d
    return int(ans*65536)


if __name__ == '__main__':
    str1,str2,expected='FRANCE','french',16384
    print(f'-input-\n  string1 : {str1}, string2 : {str2}')
    print(f'-output-\n expected : {expected}, result : {solution(str1,str2)}')



