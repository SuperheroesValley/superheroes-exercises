vector<int> Solution::searchRange(const vector<int> &A, int B) {
    vector<int> sol;
    auto it = lower_bound(A.begin(), A.end(), B);
    if (it == A.end() || *it != B)
        sol.push_back(-1);
    else
        sol.push_back(it-A.begin());
    auto it2 = upper_bound(it, A.end(), B);
    --it2;
    if (*it2 == B)
        sol.push_back(it2-A.begin());
    else
        sol.push_back(-1);
    
    return sol;
}
