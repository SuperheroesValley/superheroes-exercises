# ---------------------------------------------------------------------
# Top - Down solution
# ---------------------------------------------------------------------

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid[0])
        n = len(grid)
        dp_grid = [[None]*m for i in range(n)]
        ret = self.min_path_sum_rec(grid, 0, 0, m, n, dp_grid)
        return ret

    def min_path_sum_rec(self, grid, column, row, m, n, dp_grid):
        # If we are outside the grid
        if column >= m or row >= n:
            return float("inf")
        
        # If we are in the bottom right position
        if column == m-1 and row == n-1:
            dp_grid[row][column] = grid[row][column]
            return grid[row][column]
        
        if dp_grid[row][column]:
            return dp_grid[row][column]
        
        # We call min_path_sum_rec on the (row, column + 1) and on 
        # (row + 1, column)
        cost_1 = self.min_path_sum_rec(grid, column + 1, row, m, n, dp_grid) 
        cost_2 = self.min_path_sum_rec(grid, column, row + 1, m, n, dp_grid)
        
        dp_grid[row][column] = min(cost_1, cost_2) + grid[row][column]
        
        return dp_grid[row][column]
