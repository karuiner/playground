#k번째수
def solution(array, commands):
    answer = []
    for t in commands:
        i,j,k =t
        p=array[i-1:j]
        p.sort()
        answer.append(p[k-1])
        
    return answer

if __name__ == '__main__':
    array=[1,5,2,6,3,7,4]
    commands=[[2,5,3],[4,4,1],[1,7,3]]
    expected=[5,6,3]
    print(f'-input-\n array : {array}, commands : {commands}')
    print(f'-output-\n expected : {expected}, result : {solution(array,commands)}')

