class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Queue:
    def __init__(self):
        self.fornt = None
        self.rear = None

    def enqueue(self,value):
        new_node = Node(value)

        if self.rear == None:
            self.fornt = new_node
            self.rear = self.fornt

        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.fornt == None:
            return "Empty"
        
        else:
            self.fornt = self.fornt.next
  
    def traverse(self):
        temp = self.fornt

        while temp!=None:
            print(temp.data,end=" ")

            temp = temp.next


q = Queue()

q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.traverse()
q.dequeue()
print()
q.traverse()