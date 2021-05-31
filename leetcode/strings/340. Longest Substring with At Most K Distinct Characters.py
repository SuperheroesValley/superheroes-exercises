#Sliding window approach
#Leetcode (premium): https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
#Lintcode: https://www.lintcode.com/problem/386/description

class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
      
      l = r = 0
      max_length = 0
      unique = {}
      n = len(s) 
      
      while r < n:
        if unique.get(s[r]):
          unique[s[r]] += 1
        else:
          unique[s[r]] = 1
                 
        while len(unique.keys()) > k:
          unique[s[l]] -= 1
          if unique[s[l]] == 0:
            unique.pop(s[l])
          l+=1
        	
        max_length = max(max_length, r-l+1)
        r+=1
      
      return max_length
    
    #Possibili miglioramenti:
    #Se si usano solo le lettere dell'alfabeto, usare array invece di dictionary così da evitare le collisioni e le complessità ammortizzate
