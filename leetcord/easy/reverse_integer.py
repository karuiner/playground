class Solution:
    def reverse(self, x: int) -> int:
        y=int(''.join([i for i in str(abs(x))[::-1]]))
        if x >= 0:
            return y if y <= (2**31) -1 else 0 
        else:
            return -y if -y >= -(2**31) else 0
           

if __name__ == '__main__':
    a=Solution()
    print(a.reverse(123))
