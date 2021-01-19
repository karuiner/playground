class Solution:
    def isPalindrome(self, x: int) -> bool:
        def tt(n,s=0):
            return tt(n//10 ,s=s*10 +n%10) if n> 0 else s
        return x == tt(x)



if __name__ == '__main__':
    a=Solution()
    x=121
    ex=True
    print(f'input : {x}')
    print(f'expected : {ex}, result : {a.isPalindrome(x)}')
