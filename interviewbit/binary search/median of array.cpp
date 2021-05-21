// https://www.youtube.com/watch?v=KNviwfDeRKg
double findMedianSortedArrays(const vector<int> &A, const vector<int> &B) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details

    int N {(int)A.size()};
    int M {(int)B.size()};
    // med is the index starting from 1 of the median of the merged array
    int med {(N+M)/2};
    
    bool isOdd {(N+M) % 2 == 1};
    if (isOdd)
        ++med;
    
    // Trivial cases
    if (N == 0) {
        if (isOdd)
            return (double)(B[M/2]);
        else
            return ((double)(B[M/2 - 1] + B[M/2]))/2;
    }
    if (M == 0) {
        if (isOdd)
            return (double)(A[N/2]);
        else
            return ((double)(A[N/2 - 1] + A[N/2]))/2;
    }
    
    auto checkRet = [&] (int m, int a, int b) {
        if (isOdd)
            return (double)m;
        if (a < 0 || a >= A.size())
            return ((double)m + B[b])/2;
        if (b < 0 || b >= B.size())
            return ((double)m + A[a])/2;
        
        return ((double)m + min(A[a],B[b]))/2;
    };
    
    int l{0}, r{(int)A.size()};
    while (l <= r) { // primo incluso, ultimo escluso
        int m {(l+r)/2};
        if (m == r)
            --m;
        if (m < l)
            break;
        
        // s2 is the *exact* number of how many elements from B must be inserted before the chosen median
        int s2 {med - (m+1)}; // m is starting from zero
        
        
        if (s2 < 0)
            r = m;
        else if (s2 > B.size())
            l = m+1;
        else {
            // check if we have excactly s2 numbers in B before A[m]
            if (s2 == B.size() && B[s2-1] <= A[m])
                return checkRet(A[m], m+1, -1);
            if (s2 == 0 && B[0] >= A[m])
                return checkRet(A[m], m+1, 0);
            if (s2 > 0 && s2 < B.size() && B[s2] >= A[m] && B[s2-1] <= A[m])
                return checkRet(A[m], m+1, s2);
            
            // else we need to search on the left or on the right
            if (s2 == B.size())
                l = m+1; // search on the right
            if (s2 == 0)
                r = m; // search on the left
            if (s2 > 0 && s2 < B.size() && B[s2-1] > A[m])
                l = m+1; // search on the right
            if (s2 > 0 && s2 < B.size() && B[s2-1] <= A[m] && B[s2] < A[m])
                r = m; // search on the left
        }
    }
    
    // We didn't find a solution in array A
    // so we search it in array B
    return findMedianSortedArrays(B, A);
}
