class DynamicArray {
    private int[] container;
    private int size = 0;
    public DynamicArray(int capacity) {
        container = new int[capacity];
    }

    public int get(int i) {
        return container[i];
    }

    public void set(int i, int n) {
        container[i] = n;
    }

    public void pushback(int n) {
        if (size == container.length) {
            resize();
        }
        container[size] = n;
        size++;
    }

    public int popback() {
        size--;
        return container[size];
    }

    private void resize() {
        int[] newArray = new int[container.length * 2];
        for (int index = 0; index < newArray.length; index++) {
            if (index < size) {
                newArray[index] = container[index];
            }
        }
        container = newArray;
    }

    public int getSize() {
        return size;
    }

    public int getCapacity() {
        return container.length;
    }
}
