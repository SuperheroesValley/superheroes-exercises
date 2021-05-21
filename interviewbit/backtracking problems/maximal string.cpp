void resolve(string A, int B, int i, vector<string> &sol)
{
    if (B == 0 || i == (int)A.size()) {
        sol.push_back(A);
        return;
    }
    pair<char, vector<int>> m{A[i], vector<int>{i}};
    for (int k=i+1; k < (int)A.size(); ++k) {
        if (A[k] > m.first)
            m = {A[k], vector<int>{k}};
        else if (A[k] == m.first)
            m.second.push_back(k);
    }
    
    if (m.first == A[i]) {
        resolve(A, B, i+1, sol);
        return;
    }
    for (int k=0; k < m.second.size(); ++k) {
        swap(A[i], A[m.second[k]]);
        resolve(A, B-1, i+1, sol);
        swap(A[i], A[m.second[k]]);
    }
}

string Solution::solve(string A, int B) {
    vector<string> sol;
    resolve(A, B, 0, sol);
    
    sort(sol.rbegin(), sol.rend());
    
    return sol[0];
}
