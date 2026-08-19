from collections import Counter
class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        c=Counter(s)

        return len(set(c.values()))==1

