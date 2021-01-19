from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]

nums=[2,7,11,15]
target=9
a=Solution
print(f'input : {nums} , {target}')
print(f'result : {a.twoSum(a,nums,target)}')
