import hash_table as ht

class DigitalLibrary:
    # DO NOT CHANGE FUNCTIONS IN THIS BASE CLASS
    def __init__(self):
        pass
    
    def distinct_words(self, book_title):
        pass
    
    def count_distinct_words(self, book_title):
        pass
    
    def search_keyword(self, keyword):
        pass
    
    def print_books(self):
        pass
    
class MuskLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE
    def __init__(self, book_titles, texts):
        self.library = []
        for title, words in zip(book_titles, texts):
            words = self.mergesort(words)
            unique_words = []

            i = 0
            while i<len(words):
                temp = words[i]
                unique_words.append(words[i])
                while i<len(words) and temp==words[i]:
                    i+=1
    
            self.library.append((title, unique_words))
        self.library = self.mergesort(self.library)
        pass
    
    def distinct_words(self, book_title):
        l = 0
        r = len(self.library)-1
        while l<r:
            mid = (l+r+1)//2
            if self.library[mid][0]<=book_title:
                l = mid
            else:
                r = mid-1
        return self.library[l][1]
        pass
    
    def count_distinct_words(self, book_title):
        l = 0
        r = len(self.library)-1
        while l<r:
            mid = (l+r+1)//2
            if self.library[mid][0]<=book_title:
                l = mid
            else:
                r = mid-1
        
        return len(self.library[l][1])
        pass
    
    def search_keyword(self, keyword):
        ans = []
        for ele in self.library:
            l = 0
            r = len(ele[1])-1
            while l<r:
                mid = (l+r+1)//2
                if ele[1][mid]<=keyword:
                    l = mid
                else:
                    r = mid-1
            if ele[1][l]==keyword:
                ans.append(ele[0])
        return ans
        pass
    
    def print_books(self):
        for ele in self.library:
            print(ele[0], end=': ')
            print(' | '.join(ele[1]))
        pass
    
    def mergesort(self, arr):
        return self._mergesort(arr, 0, len(arr)-1)

    def _mergesort(self, arr, l, r):
        if l==r: return [arr[l]]
        mid = (l+r)//2
        l1 = self._mergesort(arr, l, mid)
        l2 = self._mergesort(arr, mid+1, r)
        return self.merge(l1, l2)

    def merge(self, l1, l2):
        ptr1 = 0
        ptr2 = 0
        ans = []
        while ptr1<len(l1) and ptr2<len(l2):
            if(l1[ptr1]<l2[ptr2]):
                ans.append(l1[ptr1])
                ptr1+=1
            else:
                ans.append(l2[ptr2])
                ptr2+=1
        
        while ptr1<len(l1):
            ans.append(l1[ptr1])
            ptr1+=1
        
        while ptr2<len(l2):
            ans.append(l2[ptr2])
            ptr2+=1
        
        return ans

class JGBLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE
    def __init__(self, name, params):
        '''
        name    : "Jobs", "Gates" or "Bezos"
        params  : Parameters needed for the Hash Table:
            z is the parameter for polynomial accumulation hash
            Use (mod table_size) for compression function
            
            Jobs    -> (z, initial_table_size)
            Gates   -> (z, initial_table_size)
            Bezos   -> (z1, z2, c2, initial_table_size)
                z1 for first hash function
                z2 for second hash function (step size)
                Compression function for second hash: mod c2
        '''
        self.library = None
        self.books = []
        self.params = params
        if name == "Jobs":
            self.library = ht.HashMap("Chain", params)
        elif name == "Gates":
            self.library = ht.HashMap("Linear", params)
        elif name == "Bezos":
            self.library = ht.HashMap("Double", params)
        pass
    
    def add_book(self, book_title, text):
        self.books.append(book_title)
        collision_type = self.library.collision_type
        temp = ht.HashSet(collision_type, self.params)
        for word in text:
            temp.insert(word)
        self.library.insert((book_title, temp))
        pass
    
    def distinct_words(self, book_title):
        st = self.library.find(book_title).table
        ans = []
        for ele in st:
            for words in ele:
                ans.append(words)
        return ans
        pass
    
    def count_distinct_words(self, book_title):
        return self.library.find(book_title).elements
        pass
    
    def search_keyword(self, keyword):
        ans = []
        for book in self.books:
            texts = self.library.find(book)
            if texts.find(keyword):
                ans.append(book)
        return ans
        pass
    
    def print_books(self):
        for ele in self.library.table:
            for entry in ele:
                print(entry[0], end=': ')
                print(entry[1])
        pass