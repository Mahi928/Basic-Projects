from prime_generator import get_next_size

class HashTable:
    def __init__(self, collision_type, params):
        '''
        Possible collision_type:
            "Chain"     : Use hashing with chaining
            "Linear"    : Use hashing with linear probing
            "Double"    : Use double hashing
        '''
        self.z = params[0]
        self.table_size = params[-1]
        self.table = [[] for _ in range(self.table_size)]
        self.collision_type = collision_type
        self.elements = 0
        if(collision_type=="Double"):
            self.z2 = params[1]
            self.c2 = params[2]
        pass
    
    def insert(self, x):
        if self.collision_type!="Chain" and self.table_size == self.elements:
            raise Exception("Table is full")

        key = x
        if isinstance(x, tuple):
            key = x[0]
        if self.find(key) is None or self.find(key) is False:
            slot = self.get_slot_for_insertion(key)
            
            self.table[slot].append(x)
            self.elements+=1
        pass
    
    def find(self, key):
        pass
    
    def get_slot(self, key):
        h1 = self.compute_func(self.z, key)
        slot = h1 % self.table_size
        return slot
        pass
    
    def get_load(self):
        return self.elements/self.table_size
        pass
    
    def __str__(self):
        temp = []
        for ele in self.table:
            if not ele:
                temp.append("<EMPTY>")
            else: temp.append(" ; ".join([str(entry) for entry in ele]))
        return " | ".join(temp)
        pass
    
    # TO BE USED IN PART 2 (DYNAMIC HASH TABLE)
    def rehash(self):
        pass

    def p(self, val):
        if ord(val)-ord('a')>=0:
            return ord(val)-ord('a')
        return ord(val)-ord('A')+26
    
    def compute_func(self, z, s):
        n = len(s)
        f = 0
        temp = n-1
        while temp>=0:
            f = self.p(s[temp])+z*f
            temp-=1
        return f
    
# IMPLEMENT ALL FUNCTIONS FOR CLASSES BELOW
# IF YOU HAVE IMPLEMENTED A FUNCTION IN HashTable ITSELF, 
# YOU WOULD NOT NEED TO WRITE IT TWICE
    
class HashSet(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        pass
    
    def insert(self, key):
        super().insert(key)
        pass
    
    def find(self, key):
        slot = self.get_slot(key)

        if key in self.table[slot]:
            return True
        if self.collision_type == "Chain":
            return False
        
        step = 1
        temp = slot

        if self.collision_type=="Double":
            h2 = self.compute_func(self.z2, key)
            step = self.c2 - h2%self.c2
            
        slot = (slot+step)%self.table_size
        while self.table[slot] and slot!=temp:
            if self.table[slot][0]==key: return True
            slot = (slot+step)%self.table_size

        return False
        pass
    
    def get_slot(self, key):
        return super().get_slot(key)

    def get_slot_for_insertion(self, key): # is this giving me slot even if key is there?
        slot = self.get_slot(key)

        if self.collision_type=="Chain" or not self.table[slot] :
            return slot
        
        step = 1
        temp = slot

        if self.collision_type=="Double":
            h2 = self.compute_func(self.z2, key)
            step = self.c2 - h2%self.c2
            
        slot = (slot+step)%self.table_size
        while self.table[slot] and slot!=temp:
            slot = (slot+step)%self.table_size
        return slot
        pass
    
    def get_load(self):
        return super().get_load()
        pass
    
    def __str__(self):
        temp = []
        for ele in self.table:
            if not ele:
                temp.append("<EMPTY>")
            else: temp.append(" ; ".join(ele))
        return " | ".join(temp)
        pass
    
class HashMap(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        pass
    
    def insert(self, x):
        # x = (key, value)
        super().insert(x)
        pass
    
    def find(self, key):
        slot = self.get_slot(key)
        
        for tup in self.table[slot]:
            if tup[0]==key:
                return tup[1]
        if self.collision_type == "Chain":
            return None
        
        step = 1
        temp = slot

        if self.collision_type=="Double":
            h2 = self.compute_func(self.z2, key)
            step = self.c2 - h2%self.c2

        slot = (slot+step)%self.table_size
        while self.table[slot] and slot!=temp:
            if self.table[slot][0][0]==key: return self.table[slot][0][1]
            slot = (slot+step)%self.table_size

        return None
        pass
    
    def get_slot(self, key):
        return super().get_slot(key)

    def get_slot_for_insertion(self, key):
        slot = self.get_slot(key)

        if not self.table[slot] or self.collision_type=="Chain":
            return slot

        step = 1
        temp = slot

        if self.collision_type=="Double":
            h2 = self.compute_func(self.z2, key)
            step = self.c2 - h2%self.c2

        slot = (slot+step)%self.table_size
        while self.table[slot] and slot!=temp:
            slot = (slot+step)%self.table_size
        return slot
        pass
    
    def get_load(self):
        return super().get_load()
        pass
    
    def __str__(self):
        temp = []
        for ele in self.table:
            if not ele:
                temp.append("<EMPTY>")
            else: temp.append(" ; ".join(f"({ele1}, {ele2})" for ele1, ele2 in ele))
        return " | ".join(temp)
        pass