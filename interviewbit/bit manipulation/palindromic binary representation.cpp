int Solution::solve(int A) {
    if (A == 1)
        return 1;
    if (A == 2)
        return 3;
    A -= 2;
    int n{3};
    int p{2};
    while (A > 0) {
        A -= p;
        if (A > 0) {
            ++n;
            if (n % 2 == 1)
                p *= 2;
        }
    }
    
    A += p;
    
    int m{n-n/2-1};
    vector<int> r(m, 0);
    while (--A) {
        int c {0};
        ++r[0];
        for (int k = 0; k < m; ++k) {
            r[k] = r[k] + c;
            c = (r[k] > 1 ? 1 : 0);
            r[k] %= 2;
        }
    }
    p = 2;
    int res{1};
    for (int k=m-1; k >=0; --k) {
        res += r[k] * p;
        p *= 2;
    }
    int s{0};
    if (n % 2 == 1)
        s = 1;
    for (int k=s; k < m; ++k) {
        res += r[k] * p;
        p *= 2;
    }
    res += p;
    
    return res;
}
