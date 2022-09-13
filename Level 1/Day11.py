class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.append(0)
        stair = len(cost) - 3
        memo = {}
        memo[stair+2] = 0
        memo[stair+1] = cost[stair+1]

        while(stair >= 0):
            memo[stair] = cost[stair] + min(memo[stair+1], memo[stair+2])
            stair -= 1

        return min(memo[0], memo[1])

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def calculate(row, col, memo = {}):
            if row == 1 or col == 1:
                return 1
            try:
                return memo[(row, col)]
            except KeyError:
                result = calculate(row-1, col, memo) + calculate(row, col-1, memo)
                memo[(row, col)] = result
                return result

        return calculate(m, n)

    def uniquePaths_loop(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        row = [1] * n

        for i in range(m-1):
            new_row = [1] * n
            for j in range(n-2, -1, -1):
                new_row[j] = new_row[j+1] + row[j]

            row = new_row

        return row[0]


sol = Solution()
print(sol.uniquePaths(3,7))