class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]

        for _ in range(rowIndex):
            new_row = [1]

            for j in range(len(row) - 1):
                new_row.append(row[j] + row[j + 1])

            new_row.append(1)
            row = new_row

        return row