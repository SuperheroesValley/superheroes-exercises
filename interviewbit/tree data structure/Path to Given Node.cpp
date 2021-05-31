/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 
vector<int> path;

bool dfs(TreeNode *A, int B)
{
    if (A == NULL)
        return false;
    
    path.push_back(A->val);
    
    if (A->val == B)
        return true;
    
    if (dfs(A->left, B))
        return true;
    if (dfs(A->right, B))
        return true;
    
    path.pop_back();
    return false;
}
 
vector<int> Solution::solve(TreeNode* A, int B) {
    path.clear(); // This is needed to clear the vector if it has been used before
    // DFS (Depth First Search)
    dfs(A, B);
    
    return path;
}
