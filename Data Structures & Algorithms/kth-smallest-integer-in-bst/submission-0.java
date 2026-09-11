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
    public int kthSmallest(TreeNode root, int k) {
        int[] count = new int[1];
        count[0] = 0;
        return helper(root, k, count).val;   
    }

    private TreeNode helper(TreeNode node, int k, int[] count) {
        if (node == null) {
            return null;
        } else {
            TreeNode left = helper(node.left, k , count);
            if (left != null) {
                return left;
            }
            count[0]++;
            if (count[0] == k) {
                return node;
            }
            TreeNode right = helper(node.right, k, count);
            if (right != null) {
                return right;
            }
            return null;
        }
    }
}
