class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        for i in range(len(nums)):
            if len(str(nums[i]))%2==0:
                c+=1
        
        return c
            
        