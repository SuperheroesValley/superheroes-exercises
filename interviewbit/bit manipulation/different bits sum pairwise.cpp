int Solution::cntBits(vector<int> &A) {
    long long s{0};
    int N{(int)A.size()};
    int m {(int)1e9+7};
    for (int n=0; n < 32; ++n) {
        long long n1{0};
        for (int k = 0; k < N; ++k)
            n1 += ((A[k]>>n) & 1);
        s = (s + 2*n1*(N-n1)) % m;
    }
    return s;
}
