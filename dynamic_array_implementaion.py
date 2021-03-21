import ctypes

class DynamicArray(object):

    def __init__ (self):
        self.size = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.size
    
    def __getitem__(self, k):

        if not(0<=k<self.size):
            return IndexError('Index out of bound')
        
        return self.A[k]
    
    def append(self, element):
        if self.size == self.capacity:
            self._resize(2*self.capacity)
        
        self.A[self.size] = element
        self.size += 1
    

    def _resize(self, new_capacity):

        B = self.make_array(new_capacity)

        for i in range(self.size):
            B[i] = self.A[i]

        self.A = B
        self.capacity = new_capacity
    
    def make_array(self, new_capacity):

        return (new_capacity* ctypes.py_object)()



if __name__ == "__main__":

    arr = DynamicArray()
    print(len(arr))

    arr.append(1)
    print(len(arr))

    arr.append(2)
    print(len(arr))







