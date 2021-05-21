/**
 * Definition for an interval.
 * struct Interval {
 *     int start;
 *     int end;
 *     Interval() : start(0), end(0) {}
 *     Interval(int s, int e) : start(s), end(e) {}
 * };
 */
vector<Interval> Solution::merge(vector<Interval> &A) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details

    vector<Interval> sol(A);
    vector<Interval> sol2;
    if (A.size() == 0)
        return sol2;
    sort(sol.begin(), sol.end(), [] (auto& a, auto& b) { return a.start < b.start; });
    int start{sol[0].start}, end{INT_MIN};
    for (int k=0; k < sol.size()-1; ++k) {
        end = max(end, sol[k].end);
        if (end >= sol[k+1].start) {
            end = max(end, sol[k+1].end);
        } else {
            sol2.push_back(Interval(start, end));
            end = sol[k+1].end;
            start = sol[k+1].start;
        }
    }
    sol2.push_back(Interval(start, end));
    
    return sol2;
}
