int Solution::atoi(const string A) {
    long long sol{0};
    int k;
    bool isNegative{false};
    for (k=0; k < A.size() && A[k] == ' '; ++k);
    if (A[k] == '-') {
        isNegative = true;
        ++k;
    } else if (A[k] == '+')
        ++k;
    if (A[k] < 0x30 || A[k] > 0x39)
        return 0;
    
    for (int j=k; j<A.size() && A[j] >= 0x30 && A[j] <= 0x39; ++j) {
        if (isNegative)
            sol = 10*sol - A[j]+0x30;
        else
            sol = 10*sol + A[j]-0x30;
        if (sol > INT_MAX) {
            sol = INT_MAX;
            break;
        }
        if (sol < INT_MIN) {
            sol = INT_MIN;
            break;
        }
    }
    
    return (int)sol;
}
