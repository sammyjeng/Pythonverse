#https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/1494194410/?envType=study-plan-v2&envId=top-interview-150
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
            temp = list(sorted(set(nums)))
            k = len(temp)
            z = temp+nums[k:]
            for i in range(len(nums)):
                nums[i] = z[i]
            return k
# a = Solution()
# i = [-1,0,0,0,0,3,3]
# d = a.removeDuplicates(i)
