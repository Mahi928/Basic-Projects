'''
Python Code to implement a heap with general comparison function
'''

class Heap:
    '''
    Class to implement a heap with general comparison function
    '''
    
    def __init__(self, comparison_function, init_array):
        '''
        Arguments:
            comparison_function : function : A function that takes in two arguments and returns a boolean value
            init_array : List[Any] : The initial array to be inserted into the heap
        Returns:
            None
        Description:
            Initializes a heap with a comparison function
            Details of Comparison Function:
                The comparison function should take in two arguments and return a boolean value
                If the comparison function returns True, it means that the first argument is to be considered smaller than the second argument
                If the comparison function returns False, it means that the first argument is to be considered greater than or equal to the second argument
        Time Complexity:
            O(n) where n is the number of elements in init_array
        '''
        
        # Write your code here
        self.comparator = comparison_function
        self.arr = init_array
        n = len(self.arr)//2-1
        while n>=0:
            self.downheap(n)
            n-=1
        pass
    
    def upheap(self, child):
        if child==0:
            return
        parent = (child-1)//2
        if self.comparator(self.arr[parent], self.arr[child]):
            return
        self.arr[parent], self.arr[child] = self.arr[child], self.arr[parent]
        return self.upheap(parent)
    
    def downheap(self, parent):
        n = len(self.arr)
        left_child = parent*2+1
        right_child = parent*2+2
        if left_child<n:
            child = left_child
        else: return
        if right_child<n:
            child = right_child if self.comparator(self.arr[right_child],self.arr[left_child]) else left_child
        if self.comparator(self.arr[parent], self.arr[child]):
            return
        self.arr[child], self.arr[parent] = self.arr[parent], self.arr[child]
        self.downheap(child)
        
    
    def insert(self, value):
        '''
        Arguments:
            value : Any : The value to be inserted into the heap
        Returns:
            None
        Description:
            Inserts a value into the heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        # Write your code here
        self.arr.append(value)
        child = len(self.arr)-1
        self.upheap(child)
        pass
    
    def extract(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value extracted from the top of heap
        Description:
            Extracts the value from the top of heap, i.e. removes it from heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        # Write your code here
        if len(self.arr)==0: return None
        ans = self.arr[0]
        self.arr[0] = self.arr[-1]
        self.arr.pop()
        self.downheap(0)
        return ans
        pass
    
    def top(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value at the top of heap
        Description:
            Returns the value at the top of heap
        Time Complexity:
            O(1)
        '''
        
        # Write your code here
        if len(self.arr)==0: return None
        return self.arr[0]
        pass
    
    # You can add more functions if you want to
    def size(self):
        return len(self.arr)