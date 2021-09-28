class Solution:
    def maxArea(self, height: List[int]) -> int:
        pointer_sx, pointer_dx = 0, len(height) - 1
        area = 0
        while pointer_sx < pointer_dx:
            current_area = (pointer_dx - pointer_sx)*min(height[pointer_sx], height[pointer_dx])
            if current_area > area:
                area = current_area
            if height[pointer_sx] < height[pointer_dx]:
                pointer_sx += 1
            else:
                pointer_dx -= 1
        return area
