void rSolve(vector<int> &b, vector<int> &m, vector<vector<int>> &sol, vector<int> &curr)
{
    int lastE, lastEIndex = 0;
    if (curr.size() > 0) {
        lastE = curr.back();
        auto it = lower_bound(b.begin(), b.end(), lastE);
        lastEIndex = it - b.begin();
    }
    
    sol.push_back(curr);
    
    for (int k=lastEIndex; k < (int)m.size(); ++k) {
        if (m[k] > 0) {
            curr.push_back(b[k]);
            --m[k];
            rSolve(b, m, sol, curr);
            curr.pop_back();
            ++m[k];
        }
    }
}

vector<vector<int> > Solution::subsetsWithDup(vector<int> &A) {
    vector<int> m;
    vector<int> b;
    map<int, int> buckets;
    
    for (int k=0; k < (int)A.size(); ++k)
        ++buckets[A[k]];
    
    for (auto it=buckets.begin(); it != buckets.end(); ++it) {
        m.push_back(it->second);
        b.push_back(it->first);
    }
    
    vector<vector<int>> sol;
    vector<int> curr;
    
    rSolve(b, m, sol, curr);
    
    return sol;
}
