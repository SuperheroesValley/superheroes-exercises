int Solution::isPower(int A) {
    bool isOdd{false};
    if (A < 0) {
        A = -A;
        isOdd = true;
    }
    if (A == 0 || A == 1)
        return 1;
    long long k{2};
    long long partial;
    while (k*k <= A) {
        partial = k*k;
        int e{2};
        while (partial <= A) {
            if (A == partial && !isOdd)
                return 1;
            if (A == partial && isOdd && e % 2 == 1)
                return 1;
            partial *= k;
            ++e;
        }
        ++k;
    }
    return 0;
}
