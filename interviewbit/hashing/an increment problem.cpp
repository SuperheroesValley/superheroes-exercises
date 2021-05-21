vector<int> Solution::solve(vector<int> &A) {
    unordered_map<int, priority_queue<int>> m;
    vector<int> sol;
    for (int k=0; k < A.size(); ++k) {
        if (m.count(A[k]) > 0) {    
            int p = m[A[k]].top();
            p = -p;
            m[A[k]].pop();
            m[A[k]].push(-k);
            ++sol[p];
            if (m.count(sol[p]) > 0)
                m[sol[p]].push(-p);
            else
                m[sol[p]].push(-p);
        } else
            m[A[k]].push(-k);
        sol.push_back(A[k]);
    }
    
    return sol;
}
