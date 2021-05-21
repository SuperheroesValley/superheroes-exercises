string Solution::longestCommonPrefix(vector<string> &A) {
    string comm;
    if (A.size() == 0)
        return comm;
    int s{INT_MAX};
    for (int k=0; k < A.size(); ++k)
        s = min(s, (int)A[k].size());
    for (int j=0; j < s; ++j) {
        for (int k=1; k < A.size(); ++k)
            if (A[0][j] != A[k][j])
                return comm;
        comm += A[0][j];
    }
    
    return comm;
}
