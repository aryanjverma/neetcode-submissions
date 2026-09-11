class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> counter = new HashSet<>();
        for (int num : nums) {
            if (counter.contains(num)) {
                return true;
            }
            counter.add(num);
        }
        return false;
    }
}