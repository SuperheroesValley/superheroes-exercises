"""
you are given an array A of N positive integers and an integer k.
You want to remove K consecutive elements from A such that the amplitude of remaining element is minimal.
Amplitude is the the difference between the minimal and maximal of the remaining elements.


For eg.
A = [8,8,4,3], K=2. Output should be 0.
A = [3,5,1,3,9,8], K=4,  the answer should be 1


max_l[i] = max from the start to pos. i
max_r[i] = max from the end to pos. i
"""


def min_amplitude(A, k):
    n = len(A)
    max_l = [float('-inf')]*n
    max_r = [float('-inf')]*n
    min_l = [float('inf')]*n
    min_r = [float('inf')]*n
    
    max_l[0], min_l[0] = A[0], A[0]
    max_r[-1], min_r[-1] = A[-1], A[-1]
    
    # ---->
    for i in range(1, n):
        max_l[i] = max(A[i], max_l[i-1])
        min_l[i] = min(A[i], min_l[i-1])
    
    # <----
    for i in reversed(range(n-1)):
        max_r[i] = max(A[i], max_r[i+1])
        min_r[i] = min(A[i], min_r[i+1])

    # removing the first k elements
    mag = max_r[k] - min_r[k]
    
    # excluding the subarray from start to end, bounds not included.
    # (note that between start and end there are k elements)
    start, end = 0, k+1
    while end < n:
        mag = min(mag, abs(max_l[start] - min_r[end]), abs(min_l[start] - max_r[end]))
        start += 1
        end += 1
    
    # removing the last k elements
    mag = min(mag, max_l[n-k-1] - min_l[n-k-1])
    
    return mag


print(min_amplitude([8,8,4,3], 2))
print(min_amplitude([3,5,1,3,9,8], 4))
