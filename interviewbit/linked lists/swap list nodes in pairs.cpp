/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* Solution::swapPairs(ListNode* A) {
    ListNode *p{A}, *tmp, *head{NULL}, *prev{NULL};
    while (p != NULL && p->next != NULL) {
        tmp = p->next;
        p->next = p->next->next;
        tmp->next = p;
        p = tmp;
        if (prev != NULL)
            prev->next = p;
        prev = p->next;
        if (head == NULL)
            head = p;
        
        p = p->next->next;
    }
    if (head == NULL)
        head = A;
    return head;
}
