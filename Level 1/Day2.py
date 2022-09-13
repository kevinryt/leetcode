from numpy import sort


class Solution(object):
    def isIsomorphic_fantastic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return len(set(s)) == len(set(t)) == len(set(zip(s,t)))

    def transformString(self, s: str) -> str:
        index_mapping = {}
        new_str = []
        
        for i, c in enumerate(s):
            if c not in index_mapping:
                index_mapping[c] = i
            new_str.append(str(index_mapping[c]))
        
        return " ".join(new_str)
        
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.transformString(s) == self.transformString(t)

    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n,m = len(s)-1, len(t)-1
        while (n > -1 and m > -1):
            if (s[n] == t[m]):
                n -= 1
            m -= 1
     
        # If i reaches end of s1,that mean we found all
        # characters of s1 in s2,
        # so s1 is subsequence of s2, else not
        return -1 == n
        
sol = Solution()
print(sol.isIsomorphic('aba', 'cdc'))
print(sol.isSubsequence('abc', 'aedcb'))