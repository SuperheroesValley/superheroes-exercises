int Solution::books(vector<int> &A, int B) {
    if (B > (int)A.size())
        return -1;
    
    int sum = 0;
    int l{0};
    for (auto &x : A) {
        sum += x;
        l = max(l, x);
    }
    
    auto can = [&] (auto m) {
        int b{B};
        int s{0};
        for (int k=0; k < (int)A.size() && b >= 0; ++k) {
            if (s + A[k] > m) {
                --b;
                s = 0;
            }
            s += A[k];
        }
        --b;
        if (s > m)
            --b;
        
        return b >= 0;
    };
    
    int r{sum};
    int sol = INT_MAX;
    // binary search the answer (minimum maximum number of pages of student)
    while (l <= r) {
        int m = (l+r)/2;
        
        // try left
        if (can(m)) {
            sol = m;
            r = m-1;
        
        // try right
        } else
            l = m+1;
    }
    
    return sol;
}
