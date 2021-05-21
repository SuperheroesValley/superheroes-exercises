void rSolve(string &A, int i, vector<string> &curr, vector<vector<string>> &sol)
{
    if (i == A.size()) {
        // sol
        sol.push_back(curr);
        return;
    }
    
    for (int k=i; k < (int)A.size(); ++k) {
        string s = A.substr(i, k-i+1);
        bool isP{true};
        for (int j=0; j <= s.size()/2; ++j)
            if (s[j] != s[s.size()-1-j])
                isP = false;
        if (isP) {
            curr.push_back(s);
            rSolve(A, k+1, curr, sol);
            curr.pop_back();
        }
    }
}

vector<vector<string> > Solution::partition(string A) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details

    vector<vector<string>> sol;
    vector<string> curr;
    
    rSolve(A, 0, curr, sol);
    
    return sol;
}
