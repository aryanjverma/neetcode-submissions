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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> answer = new ArrayList<>();
        if (root == null) {
            return answer;
        }
        ArrayList<TreeNode> j = new ArrayList<>();
        j.add(root);
        while (j.size() != 0) {
            int size = j.size();
            List<Integer> l = new ArrayList<>();
            for (int i = 0; i < size; i++) {
                TreeNode node = j.remove(0);
                l.add(node.val);
                if (node.left != null) {
                    j.add(node.left);
                }
                if (node.right != null) {
                    j.add(node.right);
                }
            }
            answer.add(l);
            System.out.println(answer);
        }
        return answer;
    }
}
