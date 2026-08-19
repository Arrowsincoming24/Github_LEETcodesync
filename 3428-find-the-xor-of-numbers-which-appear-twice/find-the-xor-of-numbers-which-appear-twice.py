
class Solution(object):
    def duplicateNumbersXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        answer = 0

        for number in nums:
            if number in seen:
                answer ^= number
            else:
                seen.add(number)

        return answer
        