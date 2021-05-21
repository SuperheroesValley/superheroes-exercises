string Solution::longestPalindrome(string A) {
    vector<int> d1(A.size()), d2(A.size());
    int n {A.size()};
    string sol;
    for (int k=0; k < n; ++k) {
        d1[k] = 1;
        while (k - d1[k] >= 0 && k + d1[k] < n && A[k-d1[k]] == A[k+d1[k]])
            ++d1[k];
        if (sol.size() < 2*d1[k]-1)
            sol = A.substr(k-d1[k]+1, 2*d1[k]-1);
        d2[k] = 0;
        while (k - d2[k]-1 >= 0 && k + d2[k] < n && A[k-d2[k]-1] == A[k+d2[k]])
            ++d2[k];
        if (sol.size() < 2*d2[k])
            sol = A.substr(k-d2[k], 2*d2[k]);
    }
    
    return sol;
}
