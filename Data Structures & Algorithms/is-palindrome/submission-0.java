class Solution {
    public boolean isPalindrome(String s) {
        s = getAlphaNumeric(s);
        for (int i = 0; i < (s.length() / 2); i++) {
            int j = s.length() - 1 - i;
            if (s.charAt(i) != s.charAt(j)) {
                System.out.println(s.charAt(i));
                System.out.println(s.charAt(j));
                return false;
            }
        }
        return true;
    }

    private String getAlphaNumeric(String s) {
        s = s.toLowerCase().replace(" ", "");
        return s.replaceAll("[^A-Za-z0-9]", "");
    }
}
