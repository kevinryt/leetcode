class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_sum, n = sum(nums), len(nums)
        if num_sum%2 == 1:
            return False
        
        dp = set()
        dp.add(0)
        target = num_sum // 2

        for i in range(n):
            next_dp = set()
            for t in dp:
                next_dp.add(t + nums[i])
                next_dp.add(t)
            dp = next_dp
        
        return True if target in dp else False

    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = max(nums)
        cur_min, cur_max = 1, 1

        for n in nums:
            tmp = n * cur_max
            cur_max = max(n * cur_max, n* cur_min, n)
            cur_min = min(tmp, n* cur_min, n)
            res = max(res, cur_max)
        
        return res