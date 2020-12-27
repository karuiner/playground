#프린터
def solution(priorities, location):
    t=location
    ck =True
    n=0
    while ck:
        j=priorities.index(max(priorities))
        priorities=priorities[j:]+priorities[:j]
        if j > t :
            t=len(priorities)-(j-t)
        else:
            t=t-j
        if priorities == sorted(priorities,reverse=True):
            n=n+t+1
            ck=False
        else:
            if t:
                priorities=priorities[1:]
                t-=1
                n+=1
            else:
                ck=False
                n+=1
    return n

if __name__ == '__main__':
    prio,loc,expected=[2, 1, 3, 2], 2, 1
    print(f'-input-\n priorities : {prio}, location : {loc}')
    print(f'-output-\n expected : {expected}, result : {solution(prio,loc)}')

