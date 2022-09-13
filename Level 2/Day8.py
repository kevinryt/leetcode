class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row, col = len(matrix), len(matrix[0])

        if target < matrix[0][0]:
            return False

        row_cur, col_cur = 0, 0
        while target > matrix[row_cur + 1][col_cur] and row_cur + 1 < row:
            row_cur += 1

        while col_cur < col:
            if matrix[row_cur][col_cur] == target:
                break
            row_cur += 1

        if matrix[row_cur][col_cur] == target:
            return True
        
        return False

    def searchMatrix_binary(self, matrix, target):

        row, col = len(matrix), len(matrix[0])
        low, high = 0, row * col - 1

        while low <= high:
            mid = (low + high)/2
            num = matrix[mid/col][mid%col]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid -1
        
        return False

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) / 2
            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1