from collections import Counter
class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=Counter(nums)
        sum=0
        for k,v in c.items():
            if v==1:
                sum+=k
        
        return sum
        