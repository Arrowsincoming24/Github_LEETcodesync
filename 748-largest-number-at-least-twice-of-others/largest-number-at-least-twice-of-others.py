class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = max(nums)
        idx = nums.index(x)
        nums.remove(x)

        for i in range(len(nums)):
            if x < 2 * nums[i]:
                return -1

        return idx
