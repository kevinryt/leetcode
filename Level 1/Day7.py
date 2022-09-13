class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0: return -1

        low, high = 0, len(nums)-1

        while low <= high:
            mid = (high+low)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                high = mid - 1 
            else:
                low = mid + 1
            
        return -1
    
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        while low <= high:
            pivot = (low + high)//2
            if not isBadVersion(pivot):
                low = pivot + 1 
            else:
                if not isBadVersion(pivot-1):
                    return pivot
                high = pivot - 1 

sol = Solution()
print(sol.search([-1, 0, 3, 5, 9, 12], 9))