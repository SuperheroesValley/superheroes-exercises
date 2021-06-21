# Time complexity: O(n^2)
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # Prefix sums. Formally pre[i] = the sum of nums[j] with j < i
        pre = [0]
        total = 0
        for n in nums:
            total += n
            pre.append(total)
        
        sol = 0
        
        # For each i, j consider the subarray [i,j]
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                subArraySum = pre[j+1] - pre[i]
                if subArraySum % k == 0:
                    sol += 1
        
        return sol



# Time complexity: O(n)
# Instead of saving the partial sums we can just save them modulo k
# If at some point we reach two indexes with the same partial sum modulo k then
# we know that the interval between them is divisible by k
#
# Ex:
#
# [4 5 7 3 4 5]    k = 3
# [1 0 1 1 2 1]  <--- partial sums modulo k
#  ^   ^         <--- same value
#   [5 7]        <--- subarray divisible by k 
#
#
# Why does this work?
# if we have two indexes i, j such that i < j and pre[i] == pre[j] (with 0 <= pre[.] < k)
# then we can write the sum up to i = k*A + pre[i]
# and the sum up to j = sum up to i + k*B
# so
# sum up to j = k*(A+B) + pre[i]
# if we consider the subarray ]i, j] (i excluded, j included) we have
# subarray sum = sum up to j - sum up to i
#              = k*(A+B) + pre[i] - (k*A + pre[i])
#              = k*B
# Hence we just found a subarray divisible by k
# It's easy to prove that if we have a subarray [i, j] divisible by k then pre[i-1] == pre[j]
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # Hash map, the key is the presum modulo k, the value is a frequency counter for the key
        m = {}
        # Prefix sums. Formally pre[i] = the sum of nums[j] with j < i
        pre = [0]
        m[0] = 1 # we start already we m[0] = 1
        total = 0
        for n in nums:
            total += n
            pre.append(total)
            m.setdefault(total % k, 0)
            m[total % k] += 1
        
        sol = 0
        
        # consider all the elements up to j (j excluded)
        # so j goes from 0 to len(nums)
        for j in range(len(nums)+1):
            v = pre[j]%k
            if v in m:
                # we have m[v] other indexes with the same value
                # There will always be at least one: the same pre[j]%k
                sol += m[v]
        
        # Remove all the void subarrays. There are len(nums) + 1 of them
        sol -= (len(nums) + 1)
        # We have counted all the solutions twice (if we counted [i,j] we also counted [j,i])
        sol //= 2
        
        return sol
