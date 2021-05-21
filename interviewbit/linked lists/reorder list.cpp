/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* Solution::reorderList(ListNode* A) {
    vector<int> v;
    ListNode *curr = A;
    while (curr != NULL) {
        v.push_back(curr->val);
        curr = curr->next;
    }
    
    curr = A;
    int i{0}, j{v.size()-1};
    bool p{true};
    while (curr != NULL) {
        if (p) {
            curr->val = v[i];
            ++i;
        } else {
            curr->val = v[j];
            --j;
        }
        
        p = !p;
            
        curr = curr->next;
    }
    
    return A;
}
