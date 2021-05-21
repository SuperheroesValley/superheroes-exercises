int Solution::romanToInt(string A) {
    if (A == "")
        return 0;
    
    unordered_map<char, int> m;
    m['I'] = 1;
    m['V'] = 5;
    m['X'] = 10;
    m['L'] = 50;
    m['C'] = 100;
    m['D'] = 500;
    m['M'] = 1000;
    
    int sol{0};
    int curr{m[A[0]]};
    int s{curr};
    for (int k=1; k < (int)A.size(); ++k) {
        int c = m[A[k]];
        if (s < c) { // we have to subtract
            sol -= curr;
            curr = c;
        } else if (s == c) {
            curr += c;
        } else {
            sol += curr;
            curr = c;
        }
        s = c;
    }
    sol += curr;
    
    return sol;
}
