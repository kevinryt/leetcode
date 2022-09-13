from collections import deque


class Solution(object):
    

    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        target = image[sr][sc]
        if target == color: return image

        m = len(image)
        n = len(image[0])

        def check(row, col):
            if image[row][col] == target:
                image[row][col] = color
                if row > 0:
                    check(row-1, col)
                if row < m - 1:
                    check(row+1, col)
                if col > 0:                    
                    check(row, col-1)
                if col < n - 1:
                    check(row, col+1)
        check(sr, sc)
        return image

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: return 0

        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        island = 0

        def bfs(r, c):
            q = deque()
            visit.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in direction:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and 
                        c in range(cols) and 
                        grid[r][c] == '1' and 
                        (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visit:
                    bfs(r, c)
                    island += 1
        return island


        
