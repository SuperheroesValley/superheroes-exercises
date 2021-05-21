int Solution::largestRectangleArea(vector<int> &A) {
    if (A.size() == 0)
        return 0;
    
    stack<pair<int,int>> s;
    s.push({A[0], 0});
    int m{0};
    for (int k = 1; k < (int)A.size(); ++k) {
        auto [t, pos] = s.top();
        while (A[k] < t) {
            s.pop();
            if (s.size() > 0) {
                auto [l1, pos1] = s.top();
                m = max(m, (k-pos1-1)*t);
            } else
                m = max(m, k*t);
            if (s.size() == 0)
                break;
            tie(t, pos) = s.top();
        }
        if (A[k] == t)
            s.pop();
        s.push({A[k], k});
    }
    
    while (s.size() > 0) {
        auto [t, pos] = s.top();
        s.pop();
        if (s.size() > 0) {
            auto [l1, pos1] = s.top();
            m = max(m, ((int)A.size()-pos1-1)*t);
        } else
            m = max(m, (int)A.size()*t);
    }
    
    return m;
}
