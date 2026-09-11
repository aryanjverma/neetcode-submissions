class Solution {
    public int findMin(int[] nums) {
        int low = 0;
        int mid = nums.length / 2;
        int high = nums.length - 1;
        while (low < mid && mid < high){
            if (nums[low] < nums[mid] && nums[mid] < nums[high]) {
                return nums[low];
            } else if (nums[mid] < nums[high]) {
                high = mid;
                mid = (low + mid) / 2;
            } else if (nums[low] < nums[mid]) {
                low = mid;
                mid = (mid + high) / 2; 
            }
        }
        return Math.min(nums[low], nums[high]);
    }
}
