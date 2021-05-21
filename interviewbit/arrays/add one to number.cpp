vector<int> Solution::plusOne(vector<int> &A) {
    vector<int> sol;
    int r {1};
    for (auto it = A.rbegin(); it != A.rend(); ++it) {
        sol.push_back((*it+r)%10);
        r = (*it + r)/10;
    }
    if (r == 1)
        sol.push_back(1);
    
    while (sol.size() > 0)
        if (sol.back() == 0)
            sol.pop_back();
        else
            break;
    
    reverse(sol.begin(), sol.end());
    return sol;
}
