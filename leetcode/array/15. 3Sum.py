class Solution:
    def threeSum(self, nums):
        m = {}
        p = {} # pari
        d = {} # dispari
        for k,n in enumerate(nums):
            # In questo modo evitiamo le ripetizioni di triplette uguali
            m.setdefault(n, k) # Set m[n] = k only if n not in m
            
            if n != 0: # we do not want more than one zero in the triplets
                if n > 0:
                    p[n] = k
                else:
                    d[n] = k
        
        sol = set()
        
        # The only case with more than one zero in the triplet
        if nums.count(0) >= 3:
            sol.add((0, 0, 0))
        
        
        for ni,i in p.items():
            for nj,j in d.items():
                partial = -(ni + nj)
                if partial in m and m[partial] != i and m[partial] != j:
                    sol.add(tuple(sorted([ni, nj, partial])))
        
        return sol
