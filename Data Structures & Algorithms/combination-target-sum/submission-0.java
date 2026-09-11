class Solution {
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        List<List<Integer>> answer = new ArrayList<>();
        List<Integer> curr = new ArrayList<>();
        helper(nums, target, answer, curr, 0, 0);
        return answer;
    }

    private void helper(int[] nums, int target, 
                        List<List<Integer>> answer,
                        List<Integer> curr, int sum, int index) {
        if (sum < target) {
            for (int i = index; i < nums.length; i++) {
                curr.add(nums[i]);
                helper(nums, target, answer, curr, sum + nums[i], i);
                curr.remove(curr.size() - 1);
            }
        } else if (sum == target) {
            answer.add(new ArrayList<>(curr));
        }
    }
}
