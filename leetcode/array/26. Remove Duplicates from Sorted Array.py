class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_num = -101 #out of bound
        duplicates = []
        for i in range(1,len(nums)):
            if not(nums[i] > nums[i-1]):
                duplicates.append(i)
        
        duplicates.reverse()
        for i in duplicates:
            nums.pop(i)
            
        return len(nums)
        