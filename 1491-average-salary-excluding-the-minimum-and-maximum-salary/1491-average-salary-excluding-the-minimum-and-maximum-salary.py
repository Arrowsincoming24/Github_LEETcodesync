class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        n=len(salary)
        salary.sort()
        total=0
        
        for i in range(n):
            total=total+salary[i]
        
        avg = (total-salary[0]-salary[-1])/float(n-2)

        return avg
        