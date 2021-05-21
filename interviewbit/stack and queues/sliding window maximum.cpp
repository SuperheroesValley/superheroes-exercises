vector<int> Solution::slidingMaximum(const vector<int> &A, int B) {
    deque<pair<int,int>> q;
    vector<int> sol;
    for (int k = 0; k < A.size(); ++k) {
        while (q.size() > 0 && q.back().first < A[k])
            q.pop_back();
        q.push_back({A[k], k});
        while (k - q.front().second + 1 > B)
            q.pop_front();
        if (k >= B-1)
            sol.push_back(q.front().first);
    }
    
    return sol;
}
