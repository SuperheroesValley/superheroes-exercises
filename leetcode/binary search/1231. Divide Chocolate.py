"""
https://www.lintcode.com/problem/1817/
https://leetcode.com/problems/divide-chocolate/

"""

class Solution:
  def maximizeSweetness(self, s: List[int], k: int) -> int:
    number_of_people = k + 1
    L=min(s)
    R=sum(s)//number_of_people
    
    ans=0
    while L<R:
      middle=(L+R+1)//2
      
      curr_sum=0
      cuts=0
      
      for n in s:
        curr_sum+=n
        
        if curr_sum>=middle:
          cuts+=1
          curr_sum=0
      
      if cuts>=number_of_people:
        L=middle
      else:
        R=middle-1
      
      
    return R
      
      
    
    
"""

first bad version

0000000000000111111111111
            TF

---------------------
|---|          |--|
     |-----|    |-|
   |---|    |---|
51 2 3 4 5 6 7 8 9
   L
      R
      
0:3,4,5
2:3,4
3:6
6:8,9

11111111111111111111111111111111111   k=3


 min=1
 max=45
 
middle=(45+1)//2=23
middle

             
--------------------------
EDGE CASES:
 - 


"""
