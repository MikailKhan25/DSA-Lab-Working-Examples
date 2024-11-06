class Node {
    int data;
    Node address;

    public Node(int data) {
        this.data = data;
        this.address = null;
    }
}

public class LinkedList {
    Node head;
    Node tail;

    public LinkedList() {
        head = tail = null;
    }

    public void add(int d) {
        Node n = new Node(d);

        if (head == null) {
            head = tail = n;
        } else {
            tail.address = n;
            tail = n;
        }
    }

    public void printList() {
        Node current = head;
        while (current != null) {
            System.out.println(current.data);
            current = current.address;
        }
    }

    public static void main(String[] args) {
        LinkedList list = new LinkedList();

        list.add(1);
        list.add(2);
        list.add(3);
        list.add(4);

        list.printList();
    }
}
