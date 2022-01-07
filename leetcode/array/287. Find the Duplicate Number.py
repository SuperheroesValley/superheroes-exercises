#Leetcode: https://leetcode.com/problems/find-the-duplicate-number/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = nums[0]
        slow = nums[0]
        
        #Find intersection point between slow and fast pointer
        
        #Since nums contains n+1 integers in the range [1,n]
        #the loop stops for sure thanks to the pidgeonhole th.
        #(aka, we have a cycle for sure)
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            
            if fast == slow:
                break
        
        #Find the entrance to the cycle by restarting and slowing
        #down the fast pointer
        fast = nums[0]
        while slow != fast:
            fast = nums[fast]
            slow = nums[slow]
        
        return fast
