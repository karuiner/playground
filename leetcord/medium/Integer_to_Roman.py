class Solution:
    def intToRoman(self, num: int) -> str:
        db={1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',
            50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
        ans=''
        while num:
            for i in sorted(db.keys(),reverse=True):
                if num >= i :
                    v=i
                    break
            ans+=db[v]
            num-=v
        return ans
                

a=Solution()
print(a.intToRoman(3))
