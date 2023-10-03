class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.n = 0

    def isempty(self):
        return self.top == None
    
    def push(self,value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

        self.n = self.n+1

    def traverse(self):
        curr = self.top

        while curr != None:
            print(curr.data)
            curr= curr.next

    def peek(self):
        if (self.isempty()):
            return 'Stack is empty'
        else:
            return self.top.data
        
    def pop(self):
        if self.isempty():
            return 'Stack is empty'
        else:
            self.top = self.top.next


s = Stack()
s.push(5)
s.push(6)
s.push(7)
s.push(21)
s.push(25)
s.traverse()

print(s.peek())
s.pop()
print( '--------')
s.traverse()