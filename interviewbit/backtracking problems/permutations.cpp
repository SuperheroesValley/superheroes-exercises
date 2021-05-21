int nextP(vector<int> &A)
{
    int j{A.size()-1};
    while (j > 0 && A[j] < A[j-1])
        --j;
    if (j == 0)
        return 0;
    --j;
    int i = j;
    j = (int)A.size() - 1;
    while (A[j] < A[i])
        --j;
    swap(A[i], A[j]);
    ++i;
    reverse(A.begin()+i, A.end());
    
    return 1;
}

vector<vector<int> > Solution::permute(vector<int> &A) {
    sort(A.begin(), A.end());
    vector<vector<int>> sol;
    sol.push_back(A);
    while (nextP(A))
        sol.push_back(A);
    
    return sol;
}
