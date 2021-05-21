void Solution::rotate(vector<vector<int> > &A) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    int N{A.size()};
    for (int k = 0; k < N/2; ++k) {
        // Rotate from k to N-k-1 inclusive
        for (int j=k; j < N-k-1; ++j) {
            if (N-k-k == 1)
                break;
            // A[k][j] -> A[j][N-k-1] -> A[N-k-1][N-j-1] -> A[N-j-1][k]
            swap(A[k][j], A[j][N-k-1]);
            swap(A[k][j], A[N-k-1][N-j-1]);
            swap(A[k][j], A[N-j-1][k]);
        }
    }
}
