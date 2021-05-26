string Solution::minWindow(string A, string B) {
    unordered_map<char, int> m;
    int tot = (int)B.size();
    // tells if we are taking the char at index k of string A
    vector<bool> used(A.size(), false);
    for (auto &c : B)
        ++m[c];
    
    unordered_map<char, deque<int>> got;
    int start = INT_MAX;
    int sol = INT_MAX;
    pair<int, int> best {-1, -1};
    
    for (int k=0; k < (int)A.size(); ++k) {
        // It's a interesting char
        if (m.count(A[k]) > 0) {
            // We still have to find them
            if (m[A[k]] > 0) {
                --m[A[k]];
                --tot;
                used[k] = true;
                got[A[k]].push_back(k);
                start = min(start, k);
            } else {
                used[got[A[k]].front()] = false;
                used[k] = true;
                
                // We are removing the first
                if (start == got[A[k]].front()) {
                    // search for the next first element
                    while (start <= k && !used[start])
                        ++start;
                }
                
                got[A[k]].pop_front();
                got[A[k]].push_back(k);
            }
        }
        
        if (tot == 0 && start < INT_MAX && sol > k-start+1) {
            sol = k-start + 1;
            best = {start, k};
        }
    }
    
    if (best.first == -1)
        return "";
    return A.substr(best.first, best.second-best.first+1);
}
