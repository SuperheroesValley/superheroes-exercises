/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* Solution::mergeTwoLists(ListNode* A, ListNode* B) {
    ListNode *p1{A}, *p2{B}, *n, *it;
    n = new ListNode(0);
    it = n;
    
    while (p1 != NULL && p2 != NULL) {
        if (p1->val < p2->val) {
            it->next = new ListNode(p1->val);
            it = it->next;
            p1 = p1->next;
        } else {
            it->next = new ListNode(p2->val);
            it = it->next;
            p2 = p2->next;
        }
    }
    while (p1 != NULL) {
        it->next = new ListNode(p1->val);
        it = it->next;
        p1 = p1->next;
    }
    while (p2 != NULL) {
        it->next = new ListNode(p2->val);
        it = it->next;
        p2 = p2->next;
    }
    it = n->next;
    delete(n);
    n = it;
    return n;
}
