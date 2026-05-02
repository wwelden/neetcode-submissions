class DynamicArray {
    public int[] arr;
    public int cap;
    public int size;

    public DynamicArray(int capacity) {
        arr = new int[capacity];
        cap = capacity;
        size = 0;
    }

    public int get(int i) {
        return this.arr[i];
    }

    public void set(int i, int n) {
        this.arr[i] = n;
    }

    public void pushback(int n) {
        if (this.cap == this.size){
            this.resize();
        }
        this.arr[size] = n;
        size ++;
    }

    public int popback() {
        int ret = this.arr[size-1];
        size --;
        return ret;
    }

    private void resize() {
        int[] newarr = new int[this.cap*2];
        for (int i = 0; i < this.size; i ++){
            newarr[i] = this.arr[i];
        }
        this.cap = this.cap*2;
        this.arr = newarr;
    }

    public int getSize() {
        return this.size;
    }

    public int getCapacity() {
        return this.cap;
    }
}
