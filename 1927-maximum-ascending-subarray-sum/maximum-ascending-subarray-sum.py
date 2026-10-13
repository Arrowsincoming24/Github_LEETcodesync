class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = nums[0]
        maximum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                total += nums[i]
            else:
                total = nums[i]

            maximum = max(maximum, total)

        return maximum