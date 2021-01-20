from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=''
        if len(strs) ==0 : return ''
        s=strs[0]
        for i in range(len(s)) :
            if all([s[:i+1] == j[:i+1]  for j in strs ]):
                ans=s[:i+1]
        
        return ans


a=Solution()
strs = ["flower","flow","flight"]
print(a.longestCommonPrefix(strs))
