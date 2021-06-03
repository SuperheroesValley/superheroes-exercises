class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        N = len(nums)
        if N < 2:
            return N
        
        i = 0
        j = 1
        # The array from 0 to index i does not have any duplicates
        # Search with the index j the next element in the array that is not a duplicate
        while j < N:
            if nums[i] != nums[j]: # The element nums[j] is a new element
                i += 1
                if j != i: # If it's the immediate successor of i than do not swap
                    nums[i] = nums[j]
            j += 1
        
        return i+1
