int Solution::sqrt(int A) {
    if (A == 0)
        return 0;
    if (A == 1)
        return 1;
    
    /*int l{1};
    for (long long k=2; k <= A; ++k) {
        if (k*k > A)
            return l;
        l = k;
    }*/
    
    long long l{1}, r{A};
    while (l < r) {
        long long m {(l+r)/2};
        long long e = m*m;
        if (e == A || (e < A && (m+1)*(m+1) > A))
            return (int)m;
        if (e < A)
            l = m;
        else
            r = m;
    }
}
