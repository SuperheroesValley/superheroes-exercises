# https://leetcode.com/problems/combination-sum-iii/
# TC: O(nCk*k), SC: O(k)
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def helper(k, n, start, end, path, res):
            if k == 0:
                if n == 0:
                    res.append(path[:])
                return
            
            for i in range(start, end):
                if n-i >= (k-1)*i:
                    path.append(i)
                    helper(k-1, n-i, i+1, end, path, res)
                    path.pop()
        
        res = []
        helper(k, n, 1, 10, [], res)
        return res