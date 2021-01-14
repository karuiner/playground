#전화번호 목록
def solution(b):
    ans= True
    l=[len(i) for i in b]
    for i,o in enumerate(b):
        for j,k in enumerate(b):
            if i != j: 
                if o ==k[:l[i]]:
                    ans= False
                    break
        if not ans :
            break
                
    return ans


if __name__ == '__main__':
    pb,expected=["119", "97674223", "1195524421"], False
    print(f'-input-\n  phone book : {pb}')
    print(f'-output-\n expected : {expected}, result : {solution(pb)}')



