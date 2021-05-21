int Solution::pow(int x, int n, int d) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details

    long long res{1%d}, a{x%d};
    while (n > 0) {
        if (n & 1)
            res = (res * a) % d;
        a = (a*a) % d;
        n >>= 1;
    }
    if (res < 0)
        res = res+d;
    return res;
}
