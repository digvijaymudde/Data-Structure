class Node:
    def __init__(self,value) :
        self.data=value
        self.next=None


class Linklist :
    def __init__(self) :
        #Empty Linked list
        self.head =None
        self.n = 0

    def __len__(self):
        return self.n
    
    def __str__(self):
        curr = self.head
        result = ''
        while(curr != None):
            result = result+ str(curr.data)+ '-> '
            curr = curr.next
        return result[:-3]

    def __str__(self):
        curr = self.head
        result = ''
        while(curr != None):
            result = result+ str(curr.data)+ '-> '
            curr = curr.next
        return result[:-3]

    def __str__(self):
        curr = self.head
        result = ''
        while(curr != None):
            result = result+ str(curr.data)+ '-> '
            curr = curr.next
        return result[:-3]
    
    def __getitem__(self,item):
        pos = 0
        curr = self.head

        while(curr != None):
            if item == pos :
                return curr.data
            
            curr=curr.next
            pos = pos+1
        
        return 'IndexError'
        

    def insert_head(self,value):
        new_node = Node(value)
        new_node.next =self.head
        self.head = new_node
        self.n = self.n+1

    def append(self,value):
        new_node = Node(value)

        if self.head == None:
            self.head =new_node
            self.n = self.n+1

        else:
            curr = self.head

            while(curr.next !=None):
                curr = curr.next

        # you are at last node
            curr.next = new_node
            self.n = self.n+1

    def insert_after(self,after,value):
        new_node = Node(value)
        curr = self.head

        while curr!= None:
            if curr.data == after:
                break
            curr = curr.next

        if curr!=None:
            new_node.next = curr.next
            curr.next = new_node
            self.n = self.n+1 

        else:
            return('item not found ')
        
    def clear(self):
        self.head = None
        self.n = 0

    def delete_head(self):
        if self.head == None:
            print("List is empty")
        else:
            self.head = self.head.next
            self.n = self.n-1


    def pop(self):

        curr = self.head

        if curr==None:
            return 'Empty list'

        if curr.next == None:
            self.delete_head()

        else:
            while(curr.next.next != None):
                curr = curr.next
            
            curr.next = None
            self.n = self.n-1

    def remove(self,value):

        if self.head == None:
            return 'Empty LL'
        if self.head.data == value:
            return self.delete_head()
        
        curr = self.head
        
        while curr.next != None:
            if curr.next.data == value:
                break
            curr = curr.next

        if curr.next == None:
            return 'Not found'
        
        else:
            curr.next = curr.next.next

    def search(self,item):
        pos =0
        curr = self.head

        while(curr != None):
            if curr.data == item:
                return pos
            curr =curr.next
            pos = pos +1

        return 'Not found'

#Questions:
    def replace_max(self,value):
        temp = self.head
        max = temp

        while temp!=None:
            if temp.data >max.data:
                max = temp
            temp = temp.next
        max.data = value

    def sum_odd_nodes(self):
        temp =self.head
        sum = 0
        counter = 0

        while temp!= None:
            if counter%2 == 1:
                sum = sum +temp.data
            
            counter=counter+1
            temp = temp.next
        print('Sum of odd nodes is',sum)

def main():
    L = Linklist()
    print(L)
    L.insert_head(2)
    L.insert_head(3)
    L.insert_head(4)
    L.insert_head(5)
    L.append(1)
    L.append(5)
    L.insert_after(100,100)

    print(L)
    L.clear()
    print(L)
    L.insert_head(2)
    L.insert_head(3)
    L.insert_head(20)
    L.insert_head(40)
    L.append(1)
    L.append(5)
    L.insert_after(100,100)
    print(L)
    L.remove(5)
    print(L)
    L.replace_max(5)
    L.append(4)
    print(L)
    L.sum_odd_nodes()

if __name__ =="__main__":
    main()