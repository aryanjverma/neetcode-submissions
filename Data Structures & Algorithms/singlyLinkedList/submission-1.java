class LinkedList {
    private Node head;
    private Node tail;
    private int size;
    
    public LinkedList() {
        head = null;
        tail = null;
        size = 0;
    }
    public int get(int index) {
        if (index >= size || index < 0) {
            return -1;
        }
        int currentIndex = 0;
        Node temp = head;
        while (currentIndex < index) {
            temp = temp.next;
            currentIndex++;
        }
        return temp.value;
    }

    public void insertHead(int val) {
        Node newNode = new Node(head, val);
        head = newNode;
        if (size == 0) {
            tail = newNode;
        }
        size++;
    }

    public void insertTail(int val) {
        if (size == 0) {
            insertHead(val);
        } else {
            Node newNode = new Node(null, val);
            tail.next = newNode;
            tail = newNode;
            size++;
        }
    }

    public boolean remove(int index) {
        if (index < 0 || index >= size) {
            return false;
        }
        if (index == 0) {
            head = head.next;
            size--;
            if (size == 0) {
                tail = null;
            }
            return true;
        } else if (index == size - 1) {
            Node temp = head;
            int currentIndex = 0;
            while (currentIndex < size - 2) {
                temp = temp.next;
                currentIndex++;
            }
            temp.next = null;
            tail = temp;
            size--;
            return true;
        } else {
            Node temp = head;
            int currentIndex = 0;
            while (currentIndex < index - 1) {
                temp = temp.next;
                currentIndex++;
            }
            temp.next = temp.next.next;
            size--;
            return true;
        }
    }

    public ArrayList<Integer> getValues() {
        ArrayList<Integer> values = new ArrayList<>();
        Node temp = head;
        while (temp != null) {
            values.add(temp.value);
            temp = temp.next;
        }
        return values;
    }

    private class Node {
        public Node next;
        public int value;
        public Node(Node n, int val) {
            next = n;
            value = val;
        }
    }
}
