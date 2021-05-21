int Solution::diffPossible(vector<int> &A, int B) {
    int j{0};
    for (int i=0; i < A.size(); ++i) {
        if (i == j)
            ++j;
        while (j < A.size() && A[j]-A[i] < B)
            ++j;
        if (j == A.size())
            continue;
        if (A[j]-A[i] == B)
            return 1;
    }
    
    return 0;
}
