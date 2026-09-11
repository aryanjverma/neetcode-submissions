class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int[] answer = new int[2];
        int low = 0;
        int high = numbers.length - 1;
        while (low < high) {
            if (numbers[low] + numbers[high] == target) {
                answer[0] = low + 1;
                answer[1] = high + 1;
                return answer;
            } else if (numbers[low] + numbers[high] > target) {
                high--;
            } else {
                low++;
            }
        }
        return answer;
    }
}
