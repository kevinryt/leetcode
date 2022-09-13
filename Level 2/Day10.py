from collections import deque


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        time = 0
        m, n = len(grid), len(grid[0])

        fresh = 0
        rotten = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        while rotten and fresh > 0:
            time += 1
            for _ in range(len(rotten)):
                x, y = rotten.popleft()

                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    xx = x + dx
                    yy = y + dy

                    if xx < 0 or xx == m or yy < 0 or yy == n:
                        continue

                    if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                        continue

                    fresh -= 1
                    grid[xx][yy] = 2
                    rotten.append((xx,yy))

        return time if fresh == 0 else -1

    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        row, col = len(heights), len(heights[0])
        p_visited = set()
        a_visited = set()

        def find_path(x , y, visited):
            if (x,y) in visited:
                return
            visited.add((x,y))

            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                xx = x + dx
                yy = y + dy

                if xx < 0 or xx == row or yy < 0 or yy == col:
                    continue

                if heights[x][y] <= heights[xx][yy]:
                    continue

                find_path(xx, yy, visited)

        for r in range(row):
            find_path(r, 0, p_visited)
            find_path(r, col - 1, a_visited)

        for c in range(col):
            find_path(0, c, p_visited)
            find_path(row - 1, c, a_visited)

        return (a_visited & p_visited)