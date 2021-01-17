#폰겟몬
def solution(nums):
    if len(nums)//2 > len(set(nums)):
        return len(set(nums))
    else:
        return len(nums)//2

if __name__ == '__main__':
    nums,e=[3,1,2,3],2
    print(f'-input-\n nums : {nums}')
    print(f'-output-\n expected : {e}, result : {solution(nums)}')
