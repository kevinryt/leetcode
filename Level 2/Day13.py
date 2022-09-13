class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        unrepeat = {}
        res = 0
        l = 0

        for i, char in enumerate(s):
            if char not in unrepeat:
                res = max(res, i - l + 1)
            else:
                if unrepeat[char] < l:
                    res = max(res, i - l + 1)
                else:
                    l = unrepeat[char] + 1
            unrepeat[char] = i
        
        return res

