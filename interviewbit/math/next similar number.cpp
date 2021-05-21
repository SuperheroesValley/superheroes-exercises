string Solution::solve(string A) {
    for (int k=A.size()-1; k > 0; --k) {
        if (A[k] > A[k-1]) {
            pair<int,int> best{k, A[k]};
            for (int j=k; j < A.size(); ++j)
                if (A[k-1] < A[j] && A[j] < best.second)
                    best = {j, A[j]};
            swap(A[best.first], A[k-1]);
            string B {A.substr(k)};
            sort(B.begin(), B.end());
            return A.substr(0,k)+B;
        }
    }
    return "-1";
}
