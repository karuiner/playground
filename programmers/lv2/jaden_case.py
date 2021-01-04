#jaden case 문자열 만들기
def solution(s):
    ans=''
    c=0
    for i,q in enumerate(s):
        if not i:
            if q == ' ':
                ans+=q
            else:
                if q.isalpha():
                    ans+=q.upper()
                    c+=1
                else:
                    ans+=q
                    c+=1
        else:
            if q==' ':
                ans+=q
                c=0
            else:
                if q.isalpha():
                    if c :
                        ans+=q.lower()
                        c+=1
                    else:
                        ans+=q.upper()
                        c+=1
                else:
                    ans+=q
                    c+=1
    return ans

if __name__ == '__main__':
    s,e='3people unFollowed me', '3people Unfollowed Me'
    print(f'-input-\n string : {s}')
    print(f'-output-\n expected : {e}, result : {solution(s)}')
