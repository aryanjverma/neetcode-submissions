class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        HashMap<Character, Integer> charFreqs = new HashMap<>();
        for (int index = 0; index < s.length(); index++) {
            Character sChar = s.charAt(index);
            Integer currentFrequency = charFreqs.get(sChar);
            if (currentFrequency == null) {
                currentFrequency = 0;
            }
            charFreqs.put(sChar, currentFrequency + 1);
            Character tChar = t.charAt(index);
            currentFrequency = charFreqs.get(tChar);
            if (currentFrequency == null) {
                currentFrequency = 0;
            }
            charFreqs.put(tChar, currentFrequency - 1);
            
        }
        for (Character c : charFreqs.keySet()) {
            if (charFreqs.get(c) != 0 ) {
                System.out.println(charFreqs.get(c));
                return false;
            }
        }
        return true;
    }
}
