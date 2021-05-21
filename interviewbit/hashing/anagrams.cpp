string h(string v)
{
    vector<int> o(256, 0);
    for (auto& c: v)
        ++o[c];
    
}

vector<vector<int> > Solution::anagrams(const vector<string> &A) {
    unordered_map<string, vector<int>> m;
    vector<vector<int>> sol;
    vector<string> tmpSol;
    for (int k=0; k < A.size(); ++k) {
        string hash = h(A[k]);
        if (m.count(hash) == 0)
            tmpSol.push_back(hash);
        m[h(A[k])].push_back(k);
    }
    
    for (auto& x : tmpSol)
        sol.push_back(m[x]);
    
    
    return sol;
}
