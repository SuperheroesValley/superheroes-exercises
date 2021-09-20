class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        pointer_left, pointer_right = 0, 0
        changed = 0
        ht = [0]*26
        res = 0
        
        for pointer_right in range(len(s)):
            ht[ord(s[pointer_right])-65]+=1
            changed = (pointer_right - pointer_left + 1) - max(ht)
            print(k, changed)
            while pointer_left <= pointer_right and k < changed:
                ht[ord(s[pointer_left])-65]-=1
                pointer_left += 1
                changed = (pointer_right - pointer_left + 1) - max(ht)

                
            res = max(res, pointer_right - pointer_left + 1)
        
        return res
                
