#기능개발
def solution(progresses, speeds):
    eday=[]
    for i,j in zip(progresses, speeds):
        c=((100-i)//j)+1 if (100-i)%j else (100-i)//j
        eday.append(c)
    ans=[]
    k=0
    l=0
    for i in eday:
        if len(ans):
            if i <= l:
                ans[k]+=1
            else:
                ans.append(1)
                k+=1
                l=i
        else:
            ans.append(1)
            l=i
    return ans


if __name__ == '__main__':
    progresses,speeds,expected = [93,30,55],[1,30,5],[2,1]
    print(f'-input-\n progresses : {progresses}, speeds : {speeds}')
    print(f'-output-\n expected : {expected}, result : {solution(progresses,speeds)}')

