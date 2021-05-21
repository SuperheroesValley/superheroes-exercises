/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* Solution::detectCycle(ListNode* A) {
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details
    
    ListNode *t = A;
    ListNode *h = A;
    if (A == NULL || A->next == NULL)
        return NULL;
    h = h->next;
    while (t != h) {
        if (t == NULL || h == NULL || h->next == NULL)
            return NULL;
        t = t->next;
        h = h->next->next;
    }
    t = t->next;
    
    h = A;
    while (h != t) {
        t = t->next;
        h = h->next;
    }
    
    return t;
}
