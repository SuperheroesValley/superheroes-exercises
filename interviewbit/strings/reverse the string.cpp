string Solution::solve(string A) {
    int n{A.size()};
    if (n == 0)
        return A;
    vector<string> v;
    int i{0};
    while (i < n && A[i] == ' ')
        ++i;
    int k{i};
    while (i < n) {
        if (A[i] == ' ') {
            v.push_back(A.substr(k, i-k));
            while (i < n && A[i] == ' ')
                ++i;
            k = i;
        } else
            ++i;
    }
    if (k < n)
        v.push_back(A.substr(k, i-k));
    
    if (v.size() == 0)
        return "";
    
    reverse(v.begin(), v.end());
    string out;
    for (auto& w : v) {
        out += w;
        out += " ";
    }
    out.pop_back();
    return out;
}
