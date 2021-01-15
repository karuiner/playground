#끝말잊기


def solution(n, words):
    ans=[0,0]
    u=[]
    for i,w in enumerate(words):
        if i==0:
            u.append(w)
        else:
            if u[-1][-1] != w[0]:
                ans=[(i%n)+1,(i//n)+1]
                break
            else:
                if not w in u:
                    u.append(w)
                else:
                    ans=[(i%n)+1,(i//n)+1]
                    break
    
    
    return ans




if __name__ == '__main__':
    n,words,e=3, ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank'], [3,3]
    print(f'-input-\n n : {n}, words : {words}')
    print(f'-output-\n expected : {e}, result : {solution(n,words)}')

