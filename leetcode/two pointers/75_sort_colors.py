class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        red, blue, index = 0, 0, 0
        
        for item in nums:
            if item == 0:
                red += 1
            elif item == 2:
                blue += 1
        
        white = len(nums) - red - blue
        while index < len(nums):
            if red > 0:
                nums[index] = 0
                red -= 1
            elif white > 0:
                nums[index] = 1
                white -= 1
            elif blue > 0:
                nums[index] = 2
                blue -= 1
            index += 1
        return nums
