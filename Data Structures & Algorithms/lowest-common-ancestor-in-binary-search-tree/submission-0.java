/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null) {
            return null;
        } else {
            if (root.val == p.val || root.val == q.val) {
                return root;
            } else if (root.val > p.val && root.val > q.val) {
                TreeNode answer = lowestCommonAncestor(root.left, p, q);
                if (answer != null) {
                    return answer;
                } else {
                    return root;
                }
            } else if (root.val < p.val && root.val < q.val) {
                TreeNode answer = lowestCommonAncestor(root.right, p, q);
                if (answer != null) {
                    return answer;
                } else {
                    return root;
                }
            } else {
                return root;
            }
        }
    }
}
