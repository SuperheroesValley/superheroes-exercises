vector<int> Solution::twoSum(const vector<int> &A, int B) {
    unordered_map<int, int> m;
    for (int k=(int)A.size()-1; k >= 0; --k)
        m[A[k]] = k;
    
    for (int k = 0; k < A.size(); ++k) 
        if (m.count(B-A[k]) > 0 && m[B-A[k]] < k)
            return {m[B-A[k]]+1, k+1};

    return {};
}
