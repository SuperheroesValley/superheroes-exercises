int Solution::firstMissingPositive(vector<int> &A) {
    int N{A.size()};
    for (int k=0; k < N; ++k)
        while (A[k]-1 >= 0 && A[k] < N && A[k] != A[A[k]-1])
            swap(A[A[k]-1], A[k]);
    
    for (int k=0; k < N; ++k)
        if (k != A[k]-1)
            return k+1;
    
    return N+1;
}
