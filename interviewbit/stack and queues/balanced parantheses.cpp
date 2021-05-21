int Solution::solve(string A) {
    int p{0};
    for (auto& c : A) {
        if (c == '(')
            ++p;
        else
            --p;
        if (p < 0)
            return 0;
    }
    
    return (p == 0 ? 1 : 0);
}
