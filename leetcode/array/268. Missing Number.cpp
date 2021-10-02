class Solution {
public:
    int missingNumber(vector<int>& array) {
        
        int n = array.size();
        long total_sum = (n * (n+1)) / 2;
        long partial_sum = 0;
        

        for(int i = 0; i<n; i++){
            partial_sum += array[i];
        }
        return total_sum - partial_sum;
        
    }
};