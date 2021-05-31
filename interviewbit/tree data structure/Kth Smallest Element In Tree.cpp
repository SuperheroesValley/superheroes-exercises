/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

int sol;

/* inorder traversal */
int solve(TreeNode* A, int prev, int B)

    if (A == NULL || prev >= B)
        return 0;
    
    int count {0};
    count += solve(A->left, prev, B); // left sub-tree
    ++count; // current node
    if (prev + count == B)
        sol = A->val;
    if (prev + count >= B)
        return count;
    count += solve(A->right, prev + count, B); // right sub-tree
    
    return count;
}

int Solution::kthsmallest(TreeNode* A, int B) {
    solve(A, 0, B);
    
    return sol;
}
