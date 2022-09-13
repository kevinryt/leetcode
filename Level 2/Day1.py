class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def sum_square_of_digits(num):
            sum = 0
            while (num > 0):
                sum += (num % 10)**2
                num = num // 10
            
            return sum

        result = set()
        
        while (n != 1 and n not in result):
            result.add(n)
            n = sum_square_of_digits(n)
        
        return n == 1

    def isHappy_two_pointers(self, n: int) -> bool:  
        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum

        slow_runner = n
        fast_runner = get_next(n)
        while fast_runner != 1 and slow_runner != fast_runner:
            slow_runner = get_next(slow_runner)
            fast_runner = get_next(get_next(fast_runner))
        return fast_runner == 1

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        result = []

        while left < right and top < bottom:
            # append the current top row element
            for t in range(left, right):
                result.append(matrix[top][t])
            top += 1

            # append the current right column element
            for r in range(top, bottom):
                result.append(matrix[r][right-1])
            right -= 1

            if not (left < right and top < bottom):
                break
                
            # append the current bottom row element
            for b in range(right-1, left-1, -1): 
                result.append(matrix[bottom-1][b])
            bottom -= 1

            # append the current left column element
            for l in range(bottom-1, top-1, -1):
                result.append(matrix[l][left])
            left += 1

        return result

    def findBall(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        nCols = len(grid[0])
        ballPos = {i:i for i in range(nCols)}           # Store the position of each ball

        for row in grid:
            for k, pos in ballPos.items():
                if pos == -1:                           # There's no need to check balls that are already in the deadend
                    continue
                newPos = pos + row[pos]            # The neighbor position we're going to check

				# Deadend can be formed by track directing to the boundary or the contiguous track with opposite directions
                if 0 <= newPos < nCols and row[newPos] == row[pos]:
                    ballPos[k] = newPos
                else:
                    ballPos[k] = -1
        return ballPos.values()

    def findBall_DFS(self, grid):
        ROWS = len(grid)
        COLS = len(grid[0]) 
        res = [-1 for _ in range(COLS)]
        
        def dfs(r, c):
            if r == ROWS: return c
            if grid[r][c] == 1 and (c + 1 >= COLS or grid[r][c+1] == -1):
                return -1
            elif grid[r][c] == -1 and (c - 1 < 0 or grid[r][c-1] == 1):
                return -1
            
            return dfs(r + 1, c + grid[r][c])
        
        for i in range(COLS):
            res[i] = dfs(0, i)
            
        return res

sol = Solution()
print(sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(sol.findBall([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]))