int Solution::search(const vector<int> &A, int B) {
    int l{0}, r{A.size()-1};
    bool inLeft {A[l] <= B};
    while (l < r) {
        if (r-l == 1) {
            if (A[r] == B)
                return r;
            if (A[l] == B)
                return l;
            return -1;
        }
        int m {(l+r)/2};
        if (A[m] == B)
            return m;
        if (inLeft) {
            if (A[m] < B && A[l] < A[m])
                l = m;
            else
                r = m;
        } else {
            if (A[m] > B && A[m] < A[r])
                r = m;
            else
                l = m;
        }
    }
    return -1;
}
