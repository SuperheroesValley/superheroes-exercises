# Time complexity: O(n^2)
# The solution is accepted even if it is quadratic because of the multiple optimizations
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Pre-compute the number of ones so that I can avoid calling nums.count(1) for the current subarray
        pre = [0]
        total = 0
        for n in nums:
            if n == 1:
                total += 1
            pre.append(total)
        
        ones = nums.count(1)
        zeroes = len(nums) - ones
        
        # Even-sized Sliding windows
        for i in range(2*min(ones, zeroes), 0, -2):
            l = 0
            r = i-1
            
            while r < len(nums):
                # The ones and zeroes in the subarray
                seqOnes = pre[r+1] - pre[l]
                seqZeroes = r + 1 - l - seqOnes
                diff = abs(seqZeroes - seqOnes)
                
                if diff == 0:
                    return r + 1 - l
                
                # Slides to the right by diff/2 steps
                l += diff//2
                r += diff//2
        return 0



# Time complexity: O(n)
# The idea is the following:
# By precalculating the number of ones up to index j (j excluded) we know in costant
# time the number of ones of any subarray.
# Let's consider a subarray [i, j]
# The number of ones is: seqOnes = pre[j+1] - pre[i]
# The number of zeroes is: seqZeroes = j+1 - i - seqOnes = j + 1 - i - pre[j+1] - pre[i]
#
# We want all seqOnes == seqZeroes so
# pre[j+1] - pre[i] == j + 1 - i - pre[j+1] - pre[i]
# 2*pre[j+1] - (j+1) == 2*pre[i] - i
#
# This is a nice equation where the parameters i and j are divded.
# We can use the left part of the equation as a key in a hash map and iterate over
# the i and check if we have a match.
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Hash map, the key is 2*pre[j] - j, the value is j
        m = {}
        # Pre-compute the number of ones so that I can avoid calling nums.count(1) for the current subarray
        pre = [0]
        m[0] = 0 # 2*0 - 0 -> 0
        total = 0
        for i,n in enumerate(nums):
            if n == 1:
                total += 1
            pre.append(total)
            m[2*total-(i+1)] = i+1
        
        sol = 0
        for i in range(len(nums)+1):
            v = 2*pre[i] - i # Calculate right part of the equation
            if v in m: # if we have a match then check if we have a better solution
                sol = max(sol, abs(i-m[v]))
        return sol
