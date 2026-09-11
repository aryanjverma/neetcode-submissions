class Solution {
    public String encode(List<String> strs) {
        StringBuilder b = new StringBuilder();
        for (String s : strs) {
            String length = getNum(s.length());
            b.append(length);
            b.append(s);
        }
        return b.toString();
    }

    private String getNum(int num) {
        if (num > 99) {
            return "" + num;
        } else if (num > 9) {
            return "0" + num;
        } else {
            return "00" + num;
        }
    }

    public List<String> decode(String str) {
        List<String> l = new ArrayList<>();
        int index = 0;
        while (index < str.length()) {
            int length = Integer.parseInt(str.substring(index, index + 3));
            index += 3;
            l.add(str.substring(index, index + length));
            index += length;
        }
        return l;
    }
}
