int Solution::titleToNumber(string A) {
    long long res{0};
    for (auto& c : A)
        res = res*26 + (c - 'A' + 1);
    return res;
}
