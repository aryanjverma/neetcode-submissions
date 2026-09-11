class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Set<List<Integer>> answer = new HashSet<>();
        Arrays.sort(nums);
        for (int i = 0; i < nums.length; i++) {
            int target = -1 * nums[i];
            int low = i + 1;
            int high = nums.length - 1;
            while (low < high) {
                if (target == nums[low] + nums[high]) {
                    List<Integer> l = new ArrayList<Integer>();
                    l.add(target * -1);
                    l.add(nums[low]);
                    l.add(nums[high]);
                    answer.add(l);
                    low++;
                    high--;
                } else if (target > nums[low] + nums[high]) {
                    low++;
                } else {
                    high--;
                }
            }
        }
        return new ArrayList<>(answer);
    }
}
