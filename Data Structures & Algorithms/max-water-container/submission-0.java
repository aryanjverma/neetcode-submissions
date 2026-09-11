class Solution {
    public int maxArea(int[] heights) {
        int max = 0;
        int low = 0;
        int high = heights.length - 1;
        while (low < high) {
            int lower = heights[low];
            int higher = heights[high];
            int total = (high - low) * Math.min(lower, higher);
            if (total > max) {
                max = total;
            }
            if (lower > higher) {
                high--;
            } else {
                low++;
            }
        }
        return max;
    }
}
