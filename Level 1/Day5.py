class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        r_min, gap = prices[0], 0
        for i in prices:
            if r_min > i:
                r_min = i
            elif gap < i - r_min:
                gap =  i - r_min
        return gap
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        letter = set(s)
        if len(letter) == 0:
            return 0

        length = 0;

        for i in letter:
            if s.count(i)%2==1 and length%2 !=1:
                length += 1
            length += s.count(i) - s.count(i)%2
        
        return length

        
sol = Solution()
print(sol.maxProfit([7,2,7,1,5]))