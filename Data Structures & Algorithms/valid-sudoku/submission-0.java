class Solution {
    public boolean isValidSudoku(char[][] board) {
        HashMap<Integer, HashSet<Character>> rows = new HashMap<>();
        HashMap<Integer, HashSet<Character>> cols = new HashMap<>();
        HashMap<Integer, HashSet<Character>> squares = new HashMap<>();
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board.length; j++) {
                char c = board[i][j];
                HashSet<Character> row = rows.get(i);
                HashSet<Character> col = cols.get(j);
                HashSet<Character> square = squares.get((i / 3) * 3 + (j / 3));
                if (row == null) {
                    row = new HashSet<>();
                }
                if (col == null) {
                    col = new HashSet<>();
                }
                if (square == null) {
                    square = new HashSet<>();
                }
                if (row.contains(c) || col.contains(c) || square.contains(c)) {
                    return false;
                } else if (c != '.') {
                    row.add(c);
                    col.add(c);
                    square.add(c);
                    rows.put(i, row);
                    cols.put(j, col);
                    squares.put(((i / 3) * 3 + (j / 3)), square);
                }
            }
        }
        return true;
    }
}
