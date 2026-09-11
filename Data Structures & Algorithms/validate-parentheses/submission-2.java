class Solution {
    public boolean isValid(String s) {
        Stack<Character> st = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(' || c =='[' || c == '{') {
                st.push(c);
            } else if (c == ')' && isValid('(', st)){
                return false;
            } else if (c == ']' && isValid('[', st)) {
                return false;
            } else if (c == '}' && isValid('{', st)) {
                return false;
            }
        }
        return st.isEmpty();
    }
    public boolean isValid(char c, Stack<Character> st) {
        if (st.isEmpty()) {
            return true;
        }
        return st.pop() != c;
    }
}
