class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& arr, int k) {
        int n = arr.size();
        vector <int> res;
        deque <int> window;
        int max;
        
        for(int i=0; i<n; i++){
            while((!window.empty()) && (window.front() <= i-k)){
                window.pop_front();
            }
            
            while((!window.empty()) && (arr[i] >= arr[window.back()])){
                window.pop_back();
            }
            
            window.push_back(i);
            
            
            if(i>= k-1){
                res.push_back(arr[window.front()]);
            }
        }
        return res;
    }
};