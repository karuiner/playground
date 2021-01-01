#카펫
def solution(brown, yellow):
    tn=brown+yellow
    p=[[tn//i,i] for i in range(1, int(tn**0.5)+2) if not tn%i]
    ans=[]
    for i in p:
        x,y=i
        if brown ==(2*(x+y-2)) and yellow == (x-2)*(y-2):
            ans=i
            break
    return ans

if __name__ == '__main__':
    b,y,e=10,2,[4,3]
    print(f'-input-\n brown :{b}, yellow : {y}')
    print(f'-output-\n expected : {e}, result : {solution(b,y)}')


