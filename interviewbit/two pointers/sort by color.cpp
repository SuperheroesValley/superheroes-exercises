void Solution::sortColors(vector<int> &A) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    
    // count sort
    vector<int> s(3, 0);
    for (auto& x : A)
        ++s[x];
    
    int last{0};
    for (int k=0; k < 3; ++k)
        for (int j=last; j < last+s[k]; ++j)
            A[j] = k;
}
