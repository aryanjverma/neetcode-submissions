class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>();
        for (String string : strs) {
            int[] array = getArray(string);
            String key = Arrays.toString(array);
            List<String> currentList = map.get(key);
            if (currentList == null) {
                currentList = new ArrayList<>();
            }
            currentList.add(string);
            map.put(key, currentList);
        }
        List<List<String>> answer = new ArrayList<>();
        for (String key : map.keySet()){
            answer.add(map.get(key));
        }
        return answer;
    }

    private int[] getArray(String string) {
        int[] array = new int[26];
        for (int index = 0; index < string.length(); index++) {
            char character = string.charAt(index);
            array[character - 'a']++;
        }
        return array;
    }
    private void print(int[] array) {
        for (int i : array) {
            System.out.print(i);
        }
        System.out.println();
    }
}
