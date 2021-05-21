void Solution::setZeroes(vector<vector<int> > &A) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details

    long unsigned int C {A.size()}, R {A[0].size()};
    
    unordered_set<long unsigned int> rows, columns;
    
    for (long unsigned int c=0; c < C; ++c) {
        for (long unsigned int r=0; r < R; ++r) {
            if (A[c][r] == 0) {
                rows.insert(r);
                columns.insert(c);
            }
        }
    }
    
    for (auto& c : columns) {
        for (long unsigned int r=0; r < R; ++r)
            A[c][r] = 0;
    }   
    for (auto& r : rows) {
        for (long unsigned int c=0; c < C; ++c)
            A[c][r] = 0;
    }
}
