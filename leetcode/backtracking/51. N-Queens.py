# https://leetcode.com/problems/n-queens/
#
# TC: O(n!*n^2*?*n), rispettivamente chiamate helper * check validità * foglie * conversione, unsure sia completamente corretta
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def valid(col, path):
            curr_row = len(path)
            
            if not path:
                return True
            
            for prev_row, queen in enumerate(path):
                if queen == col:
                    return False
                if  col-(curr_row-prev_row) == queen or \
                    col+(curr_row-prev_row) == queen:
                    return False
            
            return True
        
        def convert(path, n):
            new_path = []
            for queen in path:
                row = ["."]*n
                row[queen] = "Q"
                new_path.append("".join(row))
            return new_path
        
        def helper(n, path, res):
            if len(path)==n:
                res.append(convert(path, n))
                return
            
            for i in range(n):
                if (i, path):
                    path.append(i)
                    helper(n, path, res)
                    path.pop()
        
        res = []
        helper(n, [], res)
        return res