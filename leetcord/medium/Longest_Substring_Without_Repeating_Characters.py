class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mxl=0
        l=0
        db=[]
        for i in list(s):
            if not i in db:
                db.append(i)
                l+=1
            else:
                db=db[db.index(i)+1:]
                db.append(i)
                l=len(db)
            mxl=l if l > mxl else mxl
        return mxl if len(s) > 1 else len(s) 
        
        
if __name__ == '__main__':
    s="abcabcbb"
    expected=3
    a=Solution()
    print(f'input : {s}')
    print(f'expected : {expected}, result : {a.lengthOfLongestSubstring(s)}')
