class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        r=[]
        depth=0

        for ch in s:
            if ch=='(':
                if depth>0:
                    r.append(ch)
                depth+=1
            else:
                depth-=1
                if depth>0:
                    r.append(ch)

        return ''.join(r)