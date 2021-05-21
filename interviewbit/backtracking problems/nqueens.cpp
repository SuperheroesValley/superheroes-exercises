void rSolve(vector<int> &pos, int i, vector<vector<string>> &sol)
{
    if (i == pos.size()) {
        string base;
        for (int k = 0; k < i; ++k)
            base += '.';
        vector<string> curr(pos.size(), base);
        for (int k=0; k < i; ++k)
            curr[k][pos[k]] = 'Q';
        
        sol.push_back(curr);
        return;
    }
    
    for (int k=0; k < (int)pos.size(); ++k) {
        bool err{false};
        
        pos[i] = k;
        
        // check cols
        for (int j=0; j < i && !err; ++j)
            if (pos[i] == pos[j])
                err = true;
        
        int p1{k};
        int p2{k};
        // check diagonals
        for (int j=i-1; j >= 0 && !err; --j) {
            --p1;
            ++p2;
            if (pos[j] == p1 || pos[j] == p2)
                err = true;
        }
        
        if (err)
            continue;
        
        rSolve(pos, i+1, sol);
    }
}

vector<vector<string> > Solution::solveNQueens(int A) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details

    vector<vector<string>> sol;
    vector<int> pos(A, -1);
    
    rSolve(pos, 0, sol);
    
    return sol;
}
