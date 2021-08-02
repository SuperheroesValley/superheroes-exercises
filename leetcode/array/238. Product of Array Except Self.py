'''
Base solution
 Time: O(n)
 Space: O(n)
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Note: 1 is the empty product
        left_product  = [1] * n  # i-th position: product of the elements before the i-th
        right_product = [1] * n  # i-th position: product of the elements after the i-th
        
        for i in range(1, n):
            left_product[i] = nums[i-1] * left_product[i-1]
        
        for i in range(n-2, -1, -1):
            right_product[i] = nums[i+1] * right_product[i+1]
        
        output = [1] * n
        for i in range(n):
            output[i] = right_product[i] * left_product[i]
        
        return output
      
'''
Follow up
 Time: O(n)
 Space: O(1)
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_product  = 1
        right_product = 1
        output = [1] * n
        
        for i in range(1, n):
            left_product *= nums[i-1]
            output[i] = left_product
        
        for i in range(n-2, -1, -1):
            right_product *= nums[i+1]
            output[i] *= right_product

        return output
