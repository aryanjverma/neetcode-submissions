class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> indexMap = new HashMap<>();
        for (int index = 0; index < nums.length; index++) {
            int number = nums[index];
            Integer match = indexMap.get(number);
            if (match == null) {
                indexMap.put(target - number, index);
            } else {
                return new int[]{match, index};
            }
        }
        return null;
    }
}
