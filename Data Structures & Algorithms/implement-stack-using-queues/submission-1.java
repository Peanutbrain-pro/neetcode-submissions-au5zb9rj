class MyStack {
    private ArrayDeque<Integer> q1;
    private ArrayDeque<Integer> q2;

    public MyStack() {
        q1 = new ArrayDeque<>();
        q2 = new ArrayDeque<>();
    }
    
    public void push(int x) {
        q1.add(x);
    }
    
    public int pop() {
        int temp;
        while (q1.size() > 1) {
            temp = q1.remove();
            q2.add(temp);
        }
        temp = q1.remove();
        ArrayDeque<Integer> tempQueue = q1;
        q1 = q2;
        q2 = tempQueue;
        return temp;
    }
    
    public int top() {
        return q1.peekLast();
    }
    
    public boolean empty() {
        if (q1.size() <= 0)
            return true;
        else 
            return false;
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */