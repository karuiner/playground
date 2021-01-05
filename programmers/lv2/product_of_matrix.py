#행렬의 곱셈
def solution(arr1, arr2):
    def f(a,b):
        c=[i*j for i,j in zip(a,b)]
        return sum(c)
    a=[ [ f(i,j)    for j in zip(*arr2)] for i in arr1 ]
    return a

if __name__ == '__main__':
    arr1,arr2,e=[[1, 4], [3, 2], [4, 1]],[[3, 3], [3, 3]],[[15, 15], [15, 15], [15, 15]]
    print(f'-input-\n arr1 : {arr1} arr2 : {arr2}')
    print(f'-output-\n expected : {e}, result : {solution(arr1,arr2)}')

