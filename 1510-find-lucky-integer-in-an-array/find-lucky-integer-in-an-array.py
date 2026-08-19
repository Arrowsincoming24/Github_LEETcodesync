from collections import Counter
class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        c=Counter(arr)
        kmax=-1
        for k,v in c.items():
            if k==v:
                kmax=max(k,kmax)
        return kmax