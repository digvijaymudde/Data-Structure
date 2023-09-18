import ctypes

class MyList :

    def __init__(self):
        self.size = 1
        self.n = 0
        self.A = self._make_array(self.size)

    def _make_array(self,capacity):
        # create c type array(static , refrancial) with size capacity
        return(capacity*ctypes.py_object)()

    def __len__(self):
        return self.n 
    
    def __str__(self):
        result = ''
        for i in range(0,self.n):
            result = result + str(self.A[i])+ ', '

        return '['+result[:-2]+']'
         
    def __getitem__(self,index):
        
        if 0 <= index <= self.n:
            return self.A[index]
        else:
            return("IndexError - index out of range")
        
    def __delitem__(self,pos):
        if 0<=pos <=self.n: 
            for i in range(pos,self.n-1):
                self.A[i] = self.A[i+1]

            self.n = self.n-1

    def insert(self,pos,item):
        if self.n == self.size:
            self.size = self.resize(self.size*2)

        for i in range(self.n,pos,-1):
            self.A[i] = self.A[i-1]

        self.A[pos] = item
        self.n = self.n+1

    def pop(self):
        if self.n == 0:
            print("IndexError('pop from empty list')")
        else:
            print("Popping ",self.A[self.n-1])
            self.n = self.n -1

    def find(self,item):
        for i in range(0,self.n,1):
            if self.A[i] == item:
                return i 
            
        return 'ValueError - value not in list'
         
    def clear(self):
        self.n = 0
        self.size=1


    def myAppend(self,item):
        if self.n == self.size:
            #resize
            self.resize(self.size*2)

        #append 
        self.A[self.n] = item
        self.n = self.n+1

    def resize(self,new_capacity):
        B =self._make_array(new_capacity)
        self.size = new_capacity

        #copy data from A to B
        for i in range(self.n):
            B[i]= self.A[i]
        
        #reassign A
        self.A = B

    def remove(self,item):
        pos = self.find(item)
        
        if type(pos) == int:
            self.__delitem__(pos)
        else:
            return pos



def main():
    L = MyList()
 
    L.myAppend("Hello")
    L.myAppend(3)
    L.myAppend(0.3)
    L.myAppend("a")

    print(len(L))
    print(L)
    print(L[2])
    print(L[10])
     
    print(L.find("Hello"))
    L.insert(0,1)
    print(L)
    del L[3]
    print(L)
    L.remove(3)
    print(L)
if __name__ == "__main__":
    main()