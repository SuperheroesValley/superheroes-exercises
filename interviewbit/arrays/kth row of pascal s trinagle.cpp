int binomial(int n, int k)
{
    if (n == k || k == 0)
        return 1;
    return binomial(n-1, k-1) + binomial(n-1, k);
}

vector<int> Solution::getRow(int A) {
    vector<int> ans;
    int n {1};
    for (int k=0; k < A+1; ++k) {
        //~ ans.push_back(binomial(A, k)); // Sol 1
        ans.push_back(n); // Sol 2
        n = n * (A - k) / (k + 1);
    }
    
    return ans;
}
