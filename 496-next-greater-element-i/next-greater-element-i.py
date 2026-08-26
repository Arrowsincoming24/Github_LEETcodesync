class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        next_greater = {}
        stack = []

        for number in nums2:

            while stack and number > stack[-1]:
                smaller_number = stack.pop()
                next_greater[smaller_number] = number

            stack.append(number)

        answer = []

        for number in nums1:
            answer.append(next_greater.get(number, -1))

        return answer