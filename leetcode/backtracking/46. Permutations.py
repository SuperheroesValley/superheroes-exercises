# Leetcode: https://leetcode.com/problems/permutations/

class Solution:
    def perms(self, l, acc, out):
        if len(l) == 0:
            out.append(acc.copy())
        else:
            for el in l:
                acc.append(el)

                #To avoid side-effects due to pass by reference
                l_copy = l.copy()
                l_copy.remove(el)

                self.perms(l_copy, acc, out)

                #re-estabilish state after recursion expansion
                acc.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        nums = set(nums)
        out = []
        
        self.perms(nums, [], out)
        
        return out
