class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapST = {}
        mapTS = {}

        for i in range(len(s)):

            charS = s[i]
            charT = t[i]

            if charS in mapST:
                if mapST[charS] != charT:
                    return False
            if charT in mapTS:
                if mapTS[charT] != charS:
                    return False

            mapST[charS] = charT
            mapTS[charT] = charS

        return True