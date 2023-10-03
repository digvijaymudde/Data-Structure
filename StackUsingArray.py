class Stack:
    def __init__(self,size):
        self.size = size
        self.stack = [None] * self.size
        self.top = -1

    def push(self, value):
        if self.top == self.size -1:
            return 'Overflow'
        
        else:
            self.top = self.top+1
            self.stack[self.top]=value

    def pop(self):
        if self.top == -1:
            return 'empty'
        
        else:
            data  = self.stack[self.top]
            self.top-=1
            print(data)

s= Stack(4)
s.push(4)
s.push(5)
s.push(46)
s.push(3)
s.pop() 


print(s.stack)