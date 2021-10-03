class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_pointer = 0
        right_pointer = len(height) - 1
        max_area = 0
        while left_pointer < right_pointer:
            area = min(height[left_pointer], height[right_pointer])*(right_pointer - left_pointer)
            if area > max_area:
                max_area = area
            if height[left_pointer] < height[right_pointer]:
                left_pointer+=1
            else:
                right_pointer-=1
        
        return max_area