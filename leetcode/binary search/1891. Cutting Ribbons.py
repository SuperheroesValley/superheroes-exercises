"""
1891. Cutting Ribbons

https://leetcode.com/problems/cutting-ribbons/
https://www.lintcode.com/problem/183/ (should be the same exercise)

"""

class Solution:
  def maxLength(self, ribbons: List[int], k: int) -> int:
    ribbons.sort()
    L=1
    R=max(ribbons)+1
    
    ans=0
    
    while L<=R:
      
      middle=(L+R)//2
      
      curr_k=0
      for n in ribbons:
        if n<middle:continue
        
        pieces=n//middle
        curr_k+=pieces
        if curr_k>=k:break
        
      if curr_k<k:R=middle-1
      else:
        ans=max(ans,middle)
        L=middle+1
    
    
    return ans
    
