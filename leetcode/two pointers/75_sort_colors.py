'''
Soluzione 1: Insertion Sort
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        n = len(nums)
        
        for color in range(0,3):
            for i in range(j, n):
                if nums[i] == color:
                    nums[i], nums[j] = nums[j], nums[i]
                    j += 1

'''
Soluzione 2: counting sort
'''
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
