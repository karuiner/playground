# 더 맵게
def solution(scoville, K):
    def insert(arr,x):
        if len(arr) >0:
            if x <= arr[0]:
                a=0
            elif x >= arr[-1]:
                a=len(arr)
            else:
                a,b=0,len(arr)-1
                while b-a > 1:
                    c=int(0.5*(a+b))
                    if x >= arr[c]:
                        a=c
                    else:
                        b=c
        else:
            a=0
        arr.insert(a,x)
        return arr
    hx,lx=[],[]
    for i in scoville:
        if i >= K:
            insert(hx,i)
        else:
            insert(lx,i)
    ans=0
    while len(lx) > 0:
        if len(lx) ==1:
            if len(hk)>0:
                ans+=1
            else:
                ans=-1
            break
        else:
            a,b=lx[:2]
            lx=lx[2:]
            s=a+b*2
            if s >=K:
                insert(hx,s)
            else:
                insert(lx,s)
            ans+=1
    return ans


if __name__ == '__main__':
    scoville, k,expected=[1,2,3,9,10,12],7,2
    print(f'-input-\n scoville : {scoville}, K : {k}')
    print(f'-output-\n expected : {expected}, result :{solution(scoville,k)}')

