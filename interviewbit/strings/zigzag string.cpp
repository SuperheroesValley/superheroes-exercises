template <typename T>
inline T custom_ceil(T a, T b)
{
    return 1 + ((a - 1) / b);
}

string Solution::convert(string A, int B) {
    if (B==1)
        return A;
    int n{A.size()};
    int c{2*B-2};
    string out;
    for (int j=0; j < min(n,B); ++j) {
        int p{j};
        while (p < n) {
            out += A[p];
            int rPos = p % c;
            if (rPos > B-1)
                rPos -= (B-1);
            if (B-1 == rPos)
                p += (2*B - 2);
            else
                p += (B-1-rPos)*2;
        }
    }
    return out;
}
