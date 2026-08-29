class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        empty = 0

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 0:
                    empty += 1

                elif grid[r][c] == 1:
                    start_r = r
                    start_c = c

        def dfs(r, c, remain):

            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                grid[r][c] == -1):
                return 0

            if grid[r][c] == 2:
                return 1 if remain == 1 else 0

            temp = grid[r][c]
            grid[r][c] = -1

            paths = (
                dfs(r+1, c, remain-1) +
                dfs(r-1, c, remain-1) +
                dfs(r, c+1, remain-1) +
                dfs(r, c-1, remain-1)
            )

            grid[r][c] = temp

            return paths

        return dfs(start_r, start_c, empty+2)