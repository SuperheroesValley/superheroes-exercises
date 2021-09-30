class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        # Assume s1 >= s2. Otherwise invert them
        s1 = sum(nums1)
        s2 = sum(nums2)
        if s1 < s2:
            s1,s2 = s2,s1
            nums1,nums2 = nums2,nums1
        
        delta = s1 - s2
        if delta == 0:
            return 0
        
        # frequencies of the digits. Useful for sorting in O(n)
        freq1 = [0]*6
        for e in nums1:
            freq1[e-1] += 1
        
        freq2 = [0]*6
        for e in nums2:
            freq2[e-1] += 1
        
        # Only impossible condition
        if sum(freq1) > sum(freq2)*6:
            return -1
        
        # Reorder the frequencies such that the first elements are the ones that
        # have the most gain
        elements = []
        for k in range(6):
            elements.append(freq2[k])
            elements.append(freq1[5-k])
        
        res = 0
        for k in range(12):
            m = 5 - (k//2)
            # tot is how much we can gain by replacing all the elements[k] to
            # either ones or sixes (note that the gain is always the same
            # because of the way we ordered the elements)
            tot = elements[k]*m
            if delta >= tot:
                delta -= tot
                res += elements[k]
            else:
                res += (ceil(delta/m))
                delta = 0
            if delta == 0:
                return res
