int Solution::strStr(const string B, const string A) {
    if (A.size() == 0 || B.size() == 0)
        return -1;
    int n {(int)B.size()-(int)A.size()+1};
    int c{0};
    int s{0};
    while (s < n) {
        bool ok{true};
        for (int k=0; k < A.size(); ++k) {
            if (B[s+k] != A[k]) {
                ok = false;
                break;
            }
        }
        if (ok)
            return s;
        ++s;
    }
    
    return -1;
}
