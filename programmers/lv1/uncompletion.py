#완주하지 못한 선수
def solution(participant, completion):
    p,c=sorted(participant),sorted(completion)
    ans=p[-1]
    for i,ip in enumerate(c):
        if ip != p[i]:
            ans=p[i]
            return ans
    return ans

if __name__ == "__main__":
    ipt_p=["leo", "kiki", "eden"]
    ipt_c=["eden","kiki"]
    erst="leo"
    print(f'input : participant : {ipt_p}, completion : {ipt_c}')
    print(f'expected : {erst}  , result : {solution(ipt_p,ipt_c)}')

