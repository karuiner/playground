#스킬트리
def solution(skill, skill_trees):
    s=list(skill)
    n=0
    for i in skill_trees:
        c=''.join([j for j in i if (j in s)  ])
        l=len(c)
        if c == skill[:l]:
            n+=1
        
        
    answer = n
    return answer

if __name__ == '__main__':
    skill,strees,expected="CBD",["BACDE", "CBADF", "AECB", "BDA"],2
    print(f'-input-\n skill : {skill}, skill trees : {strees}')
    print(f'-output-\n expected : {expected}, result : {solution(skill,strees)}')



