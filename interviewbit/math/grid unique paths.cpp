int Solution::uniquePaths(int A, int B) {
    vector<vector<int>> dp(A, vector<int>(B));
    dp[A-1][B-1] = 1;
    
    for (int c=B-1; c >= 0; --c) {
        for (int r=A-1; r >= 0; --r) {
            if (r == A-1 && c == B-1)
                continue;
            if (r == A-1)
                dp[r][c] = dp[r][c+1];
            else if (c == B-1)
                dp[r][c] = dp[r+1][c];
            else
                dp[r][c] = dp[r+1][c] + dp[r][c+1];
        }
    }
    
    return dp[0][0];
}
