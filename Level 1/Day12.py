import collections

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        s_slice = collections.Counter(s[0 : 0 + len(p)])
        p_slice = collections.Counter(p)

        pos = [0] if s_slice == p_slice else []

        for i in range(len(s) - len(p)):
            j = i+len(p)
            s_slice[s[i]] -= 1
            s_slice[s[j]] = 1 + s_slice.get(s[j], 0)
            if s_slice[s[i]] == 0:
                s_slice.pop(s[i])
            if s_slice == p_slice:
                pos.append(i+1)

        return pos

    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = {}
        result = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            while (r - l + 1 - max(count.values()) > k):
                count[s[l]] -= 1
                l += 1
            
            result = max(result, r - l + 1)

        return result

sol = Solution()
print(sol.findAnagrams('abab', 'ab'))