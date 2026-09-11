class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> m = new HashSet<>();
        for (int num : nums) {
            m.add(num);
        }
        int max = 0;
        for (Integer num : m) {
            if (!m.contains(num - 1)) {
                int curRun = 1;
                while (m.contains(num + curRun)) {
                    curRun++;
                }
                max = Math.max(max, curRun);
            } 
        }
        return max;
    }
}
