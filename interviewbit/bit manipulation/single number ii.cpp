int Solution::singleNumber(const vector<int> &A) {
    int fix{0};
    int sum{0};
    for (auto& x : A) {
        sum ^= x;
        sum ^= (fix&x);
        fix ^= x;
        fix &= sum;
    }
    return sum;
}
