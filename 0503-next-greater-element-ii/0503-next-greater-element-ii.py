class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        answer = [-1] * length
        stack = []

        for position in range(2 * length):
            index = position % length

            while stack and nums[index] > nums[stack[-1]]:
                previous_index = stack.pop()
                answer[previous_index] = nums[index]

       
            if position < length:
                stack.append(index)

        return answer
        