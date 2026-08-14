class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)

        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            x = ord(ch) - ord('a')
            first[x] = min(first[x], i)
            last[x] = i

        intervals = []

        for c in range(26):
            if first[c] == n:
                continue

            start = first[c]
            end = last[c]
            i = start
            valid = True

            while i <= end:
                x = ord(s[i]) - ord('a')

                if first[x] < start:
                    valid = False
                    break

                end = max(end, last[x])
                i += 1

            if valid:
                intervals.append((start, end))

        intervals.sort(key=lambda x: x[1])

        ans = []
        prev_end = -1

        for start, end in intervals:
            if start > prev_end:
                ans.append(s[start:end + 1])
                prev_end = end

        return ans
        