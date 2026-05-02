public class LinkedList {
     private class Node
    {
        public int data;
        public Node next;

        public Node(int data)
        {
            this.data = data;
            this.next = null;
        }
    }
    private Node head;
    private int size;

    public LinkedList()
    {
        head = null;
        size = 0;
    }

   public int Get(int index)
    {
        if (index < 0 || index >= size)
        {
            return -1;
        }

        Node currNode = head;
        for (int i = 0; i < index; i++)
        {
            currNode = currNode.next;
        }
        return currNode.data;
    }

     public void InsertHead(int val)
    {
        Node newNode = new Node(val);
        newNode.next = head;
        head = newNode;
        size++;
    }

    public void InsertTail(int val)
    {
        Node newNode = new Node(val);

        if (head == null)
        {
            head = newNode;
        }
        else
        {
            Node currNode = head;
            while (currNode.next != null)
            {
                currNode = currNode.next;
            }
            currNode.next = newNode;
        }
        size++;
    }

     public bool Remove(int index)
    {
        if (index < 0 || index >= size)
        {
            return false;
        }

        if (index == 0)
        {
            head = head.next;
        }
        else
        {
            Node currNode = head;
            for (int i = 0; i < index - 1; i++)
            {
                currNode = currNode.next;
            }
            currNode.next = currNode.next.next;
        }
        size--;
        return true;
    }

    public List<int> GetValues()
    {
        List<int> values = new List<int>();
        Node currNode = head;
        while (currNode != null)
        {
            values.Add(currNode.data);
            currNode = currNode.next;
        }
        return values;
    }
}