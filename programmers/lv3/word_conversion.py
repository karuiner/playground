def solution(begin, target, words):
    def ckw(a,b):
        return sum([1 for i,j in zip(list(a),list(b)) if i==j])
    if target in words:
        ck=begin
        n=1
        ans=0
        while ck != target:
            swl=[i   for i in words if ckw(i,ck) == len(ck) -1]
            if len(swl) >1:
                zz=[ckw(i,target)   for i in swl ]
                ck=swl[zz.index(max(zz))]
                n=max(zz)
                ans+=1
            elif len(swl) ==1:
                ck=swl[0]
                n=ckw(ck,target)
                ans+=1
            else:
                ans=0
                break
    
    
    else:
        ans = 0
    return ans

if __name__ =='__main__':
    begin,target,words='hit','cog',['hot','dot','dog','lot','log','cog']
    expected=4
    print(f'-input-\n begin : {begin}, target : {target}, words : {words}')
    print(f'-output-\n expected : {expected}, result : {solution(begin,target,words)}')
