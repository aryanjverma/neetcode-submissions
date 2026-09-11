class Solution {
    public int[] productExceptSelf(int[] nums) {
        if (nums.length == 1 || nums.length == 0) {
            return nums;
        }
        int[] prefix = new int[nums.length];
        int[] suffix = new int[nums.length];
        for (int index = 0; index < nums.length; index++) {
            int other = nums.length - index - 1;
            prefix[index] = nums[index];
            suffix[other] = nums[other];
            if (index != 0) {
                prefix[index] *= prefix[index - 1];
                suffix[other] *= suffix[other + 1];
            }
        }
        print(prefix);
        print(suffix);
        int[] answer = new int[nums.length];
        for (int index = 0; index < nums.length; index++) {
            answer[index] = 1;
            if (index != 0) {
                answer[index] = prefix[index - 1];
            }
            if (index != nums.length - 1) {
                answer[index] *= suffix[index + 1];
            }
        }
        return answer;
    }

    private void print(int[] r) {
        for (int j : r) {
            System.out.print(j + ",");
        }
        System.out.println();
    }
}  
