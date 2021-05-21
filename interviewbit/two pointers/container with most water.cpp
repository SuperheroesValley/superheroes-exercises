int Solution::maxArea(vector<int> &A) {
    int l{0}, r{A.size()-1};
    int best{0};
    while (l < r) {
        best = max(best, min(A[l], A[r])*(r-l));
        if (A[l] < A[r])
            ++l;
        else
            --r;
    }
    return best;
}
