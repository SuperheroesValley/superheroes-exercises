vector<int> Solution::dNums(vector<int> &A, int B) {
    int N = (int)A.size();
    if (B > N)
        return {};
    
    unordered_map<int, int> c;
    int cont{0};
    vector<int> sol;
    for (int k=0; k < B; ++k) {
        ++c[A[k]];
        if (c[A[k]] == 1)
            ++cont;
    }
    
    sol.push_back(cont);
    
    for (int k=B; k < N; ++k) {
        --c[A[k-B]];
        if (c[A[k-B]] == 0)
            --cont;
        ++c[A[k]];
        if (c[A[k]] == 1)
            ++cont;
        sol.push_back(cont);
    }
    
    return sol;
}

