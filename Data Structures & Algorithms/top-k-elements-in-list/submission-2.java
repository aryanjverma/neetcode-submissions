class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        if (k == nums.length) {
            return nums;
        }
        HashMap<Integer, Integer> freqMap = new HashMap<>();
        for (int num : nums) {
            Integer currentFreq = freqMap.get(num);
            if (currentFreq == null) {
                currentFreq = 0;
            }
            currentFreq++;
            freqMap.put(num, currentFreq);
        }
        System.out.println(freqMap);
        ArrayList<Integer>[] buckets = new ArrayList[nums.length];
        for (Integer val : freqMap.keySet()) {
            Integer freq = freqMap.get(val);
            int index = nums.length - freq;
            if (buckets[index] == null) {
                buckets[index] = new ArrayList<Integer>();
            }
            buckets[index].add(val);
        }
        int[] answer = new int[k];
        if (k == 0) {
            return answer;
        }
        for (ArrayList<Integer> bucket : buckets) {
            System.out.println(bucket);
            if (bucket != null) {
                for (Integer val : bucket) {
                    k--;
                    answer[k] = val;
                    if (k == 0) {
                        return answer;
                    }
                }
            }
        }
        return answer;
    }
}