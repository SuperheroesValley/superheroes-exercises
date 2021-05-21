vector<int> Solution::wave(vector<int> &A) {
    vector<int> sol(A);
    sort(sol.begin(), sol.end());
    for (int k=0; k < sol.size()-1; k += 2)
        swap(sol[k], sol[k+1]);
    
    return sol;
}
