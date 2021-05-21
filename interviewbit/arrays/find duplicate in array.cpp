int Solution::repeatedNumber(const vector<int> &A) {
    int s{0};
    for (auto& x : A)
        s += x;
    
    s -= ((A.size())*(A.size()-1))/2;
    
    return s;
}
