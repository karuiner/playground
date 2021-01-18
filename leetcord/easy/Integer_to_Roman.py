class Solution:
    def romanToInt(self, s: str) -> int:
        db={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        b=[]
        ls=list(s)
        for i,j in zip(ls[:-1],ls[1:]):
            if db[j] >db[i]:
                b.append(-db[i])
            else:
                b.append(db[i])
        b.append(db[s[-1]]) 
        return sum(b)

if __name__ == '__main__':
    a=Solution()
    print(a.romanToInt('III'))
