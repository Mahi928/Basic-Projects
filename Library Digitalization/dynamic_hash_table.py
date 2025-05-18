from hash_table import HashSet, HashMap
from prime_generator import get_next_size

class DynamicHashSet(HashSet):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        # IMPLEMENT THIS FUNCTION
        temp = self.table
        self.table_size = get_next_size()
        self.table = [[] for _ in range(self.table_size)]
        self.elements = 0

        for ele in temp:
            for entry in ele:
                self.insert(entry)
        pass
        
    def insert(self, key):
        # YOU DO NOT NEED TO MODIFY THIS
        super().insert(key)
        
        if self.get_load() >= 0.5:
            self.rehash()
            
            
class DynamicHashMap(HashMap):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash(self):
        # IMPLEMENT THIS FUNCTION
        temp = self.table
        self.table_size = get_next_size()
        self.table = [[] for _ in range(self.table_size)]
        self.elements = 0
        
        for ele in temp:
            for entry in ele:
                self.insert(entry)
        pass
        
    def insert(self, key):
        # YOU DO NOT NEED TO MODIFY THIS
        super().insert(key)
        
        if self.get_load() >= 0.5:
            self.rehash()