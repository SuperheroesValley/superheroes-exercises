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
