'''
Pattern: Minimum/Maximum path to reach a target
Solution: 
'''
# ----------------------------------------------------------------------------------------------------
# Bottom - up solution
# ----------------------------------------------------------------------------------------------------
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        for i in range(2, n):
            cost[i] = min(cost[i-1], cost[i-2]) + cost[i]
        return min(cost[-1], cost[-2])
      
# ----------------------------------------------------------------------------------------------------
# Top - Down solution
# ----------------------------------------------------------------------------------------------------
# Example: we start with this [1, 100, 1,1,1,100,1,1,100,1]
# The first call is with current_index = 0 and current_index = 1
# Then for 0 we make another call to min_climb_recursion with current_index = 1 and current_index = # 2. For 1 we make a call to current_index with current_index = 2 and current_index = 3 and so on.
# This is how the dp array is modified by the recursion:
# [None, None, None, None, None, None, None, None, None, 1]
# [None, None, None, None, None, None, None, None, 100, 1]
# [None, None, None, None, None, None, None, 2, 100, 1]
# [None, None, None, None, None, None, 3, 2, 100, 1]
# [None, None, None, None, None, 102, 3, 2, 100, 1]
# [None, None, None, None, 4, 102, 3, 2, 100, 1]
# [None, None, None, 5, 4, 102, 3, 2, 100, 1]
# [None, None, 5, 5, 4, 102, 3, 2, 100, 1]
# [None, 105, 5, 5, 4, 102, 3, 2, 100, 1]
# [6, 105, 5, 5, 4, 102, 3, 2, 100, 1]
# [6, 105, 5, 5, 4, 102, 3, 2, 100, 1]

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [None]*len(cost)
        return min(self.min_climb_recursion(0, cost, dp), self.min_climb_recursion(1, cost, dp))
    
    def min_climb_recursion(self, current_index, cost, dp):
        # base case: if the current index is out of the array
        # we return 0
        if current_index >= len(cost):
            return 0
        
        if dp[current_index]:
            return dp[current_index]
      
        # We call min_climb_recursion on the next two elements and we add the cost of the current element
        cost_1 = self.min_climb_recursion(current_index + 1, cost, dp) + cost[current_index]
        cost_2 = self.min_climb_recursion(current_index + 2, cost, dp) + cost[current_index]
        
        dp[current_index] = min(cost_1, cost_2)
        return dp[current_index]
