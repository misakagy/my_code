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

        vector<vector<TreeNode *>> dp(N + 1);
        dp[1] = {new TreeNode(0)};
        for(int i = 3; i <= N; i += 2)
        {
            for(int j = 1; j < i; j += 2)
            {
                for(const auto &l : dp[j])
                {
                    for(const auto &r : dp[i - j - 1])
                    {
                        auto root = new TreeNode(0);
                        root->left = l;
                        root->right = r;
                        dp[i].push_back(root);
                    }
                }
            }
        }
        return dp[N];    
    }
};