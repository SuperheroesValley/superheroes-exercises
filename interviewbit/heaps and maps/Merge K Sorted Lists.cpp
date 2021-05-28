// First solution - priority queue
// Complexity: O(n*log k)
// n is the total number of elements considering all the lists
// k is number of lists
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* Solution::mergeKLists(vector<ListNode*> &A) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    
    priority_queue<pair<int, int>> q;
    ListNode* sol = nullptr;
    ListNode* curr;
    
    for (int k=0; k < (int)A.size(); ++k)
        if (A[k] != NULL)
            // by default priority_queue put on top the biggest element,
            // we want instead the smaller one
            q.push({-A[k]->val, k});
    
    while (!q.empty()) {
        auto best = q.top();
        q.pop();
        
        // We have our best choice, let's append it to our solution
        if (sol == nullptr) {
            sol = A[best.second];
            curr = sol;
        } else {
            curr->next = A[best.second];
            curr = curr->next;
        }
        
        // put the next element
        if (A[best.second]->next != NULL) {
            A[best.second] = A[best.second]->next;
            q.push({-A[best.second]->val, best.second});
        }
    }
    
    return sol;
}


// Second solution - k-way merge sort
// Complexity: O(n*k)
// n is the total number of elements considering all the lists
// k is number of lists
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* Solution::mergeKLists(vector<ListNode*> &A) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    
    ListNode* sol = nullptr;
    ListNode* curr;
    while (true) {
        // Find the best choice
        pair<int, int> best{INT_MAX, -1};
        for (int k = 0; k < (int)A.size(); ++k) {
            if (A[k] != NULL && A[k]->val < best.first)
                best = {A[k]->val, k};
        }
        
        // Exit condition
        if (best.second == -1)
            break;
        
        // We have our best choice, let's append it to our solution
        if (sol == nullptr) {
            sol = A[best.second];
            curr = sol;
        } else {
            curr->next = A[best.second];
            curr = curr->next;
        }
        A[best.second] = A[best.second]->next;
    }
    
    return sol;
}
