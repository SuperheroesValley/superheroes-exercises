/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* Solution::solve(ListNode* A) {
    ListNode *p {A};
    int z{0};
    int o{0};
    while (p != NULL) {
        if (p->val)
            ++o;
        else
            ++z;
        p = p->next;
    }
    p = A;
    while (p != NULL) {
        if (z) {
            --z;
            p->val = 0;
        } else
            p->val = 1;
        p = p->next;
    }
    return A;
}
