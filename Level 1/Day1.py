class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [nums[0]]
        for i in range(1,len(nums)):
            result.append(result[i-1] + nums[i])
    
        return result 

    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_sum = 0
        right_sum = sum(nums)
        for i in range(len(nums)):
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        
        return -1
            


sol = Solution()
print(sol.runningSum([1,2,3,4]))
print(sol.pivotIndex([1,7,3,6,5,6]))