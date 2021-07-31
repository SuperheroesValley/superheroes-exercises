'''
Soluzione 1: soluzione iterativa che per ogni elemento della lista decide se inserirlo
o meno nel subset. Per tenere conto dei gruppi che abbiamo creato si usa un set.
'''
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        subsets = set([(0 ,0, 0), (strs[0].count("0"), strs[0].count("1"), 1)])
        
        for item in strs[1:]:
            current_sub = set()
            zero = item.count("0")
            one = item.count("1")
            
            for subset in subsets:
                if subset[0] + zero <= m and subset[1] + one <= n:
                    current_sub.add((subset[0] + zeo, subset[1] + one, subset[2] + 1))
                current_sub.add(subset)
            subsets = current_sub
        
        max_value = -1
        for item in subsets:
            if item[0] <= m and item[1] <= n and item[2] > max_value:
                max_value = item[2]
                
        return max_value


'''
Soluzione 2: soluzione ricorsiva con lru_cache, in questo caso ricorsivamente 
scegliamo di includere o no un elemento della lista e contiamo
gli elementi che abbiamo inserito.
'''
from functools import lru_cache
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        counter = []
        for item in strs:
            zero = item.count("0")
            one = item.count("1")
            counter.append([zero, one])

        @lru_cache(None)
        def dp(current_zero, current_one, index):
             
            if index == len(strs):
                return 0

            not_included = dp(current_zero, current_one, index+1)
            
            zero = counter[index][0]
            one = counter[index][1]
            
            if current_zero + zero <= m and current_one + one <= n:
                included = 1 + dp(current_zero + zero, current_one + one, index+1)
                return max(included, not_included)
            else:
                return not_included
            
            
        return dp(0, 0, 0)r
