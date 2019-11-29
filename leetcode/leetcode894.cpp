/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<TreeNode*> allPossibleFBT(int N) 
    {
        if(N % 2 == 0)
        {
            /*N为偶数时为错误，直接返回空*/
            return {};
        }

        if(1 == N)
        {
            return {new TreeNode(0)};
        }

        vector<TreeNode *> ans;
        for(int i = 1; i < N; i += 2)
        {
            for(auto l : allPossibleFBT(i))
            {
                for(auto r : allPossibleFBT(N - i - 1))
                {
                    auto root = new TreeNode(0);
                    root->left = l;
                    root->right = r;
                    ans.push_back(root);
                }
            }

        }
        return ans;    
    }
};