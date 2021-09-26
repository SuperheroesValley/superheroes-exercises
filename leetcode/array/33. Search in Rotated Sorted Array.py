#Leetcode: https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #find smallest element
        def mod_bin_search(l,r):
            if l < r:
                m = (l + r) // 2
                
                #Check for k
                if m < r and nums[m] > nums[m+1]:
                    return m+1
                
                if m > l and nums[m] < nums[m-1]:
                    return m
                
                #If not found, I have to either go right or left
                if nums[m] > nums[r]: #Array seems rotated
                    return mod_bin_search(m+1, r)
                else: #Array seems sorted fine
                    return mod_bin_search(l, m-1)
            elif l > r: #Array is not rotated
                return 0
            else:
                return l
            
        def bin_search(t, l, r):
            if l <= r:
                m = (l + r) // 2
                
                if nums[m] == t:
                    return m
                elif nums[m] > t:
                    return bin_search(t, l, m-1)
                else:
                    return bin_search(t, m+1, r)
            else:
                return -1
            
        n = len(nums)
        
        #binary search the smallest element to find k
        k = mod_bin_search(0, n-1)
        
        #partition-wise binary search
        if nums[k] <= target <= nums[n-1]:
            return bin_search(target, k, n-1)
        else:
            return bin_search(target, 0, k-1)
