from node import Node

def comp_1(node_1, node_2):
    if node_1.id==node_2.id:
        return 0
    if node_2.id>node_1.id:
        return -1
    if node_1.id>node_2.id:
        return 1

#1 says go left, -1 says go right, 0 stays

class AVLTree:
    def __init__(self, compare_function=comp_1):
        self.root = None
        self.size = 0
        self.comparator = compare_function

    def traverse(self, root, s):
        if not root:
            return s
        if root.left:
            self.traverse(root.left, s)
        s.append(root.data.id)
        if root.right:
            self.traverse(root.right, s)
        return s
    
    def get_height(self, root):
        if not root:
            return -1
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def left_rotation(self, a):
        b = a.right
        t = b.left

        b.left = a
        a.right = t

        a.height = 1+max(self.get_height(a.left), self.get_height(a.right))
        b.height = 1+max(self.get_height(b.left), self.get_height(b.right))

        return b

    def right_rotation(self, a):
        b = a.left
        t = b.right

        b.right = a
        a.left = t

        a.height = 1+max(self.get_height(a.left), self.get_height(a.right))
        b.height = 1+max(self.get_height(b.left), self.get_height(b.right))

        return b

    def insert(self, root, data):
        if not root:
            temp = Node(data)
            return temp
        if self.comparator(root.data, data)==0:
            return root
        if self.comparator(root.data, data)==-1:
            root.right = self.insert(root.right, data)
        else:
            root.left = self.insert(root.left, data)
        
        root.height = max(self.get_height(root.right), self.get_height(root.left))+1

        balance = self.get_balance(root)
        
        if balance<-1:
            if self.comparator(root.right.data, data)==-1:
                return self.left_rotation(root)
            else:
                root.right = self.right_rotation(root.right)
                return self.left_rotation(root)
        
        if balance>1:
                if self.comparator(root.left.data, data)==1:
                    return self.right_rotation(root)
                else:
                    root.left = self.left_rotation(root.left)
                    return self.right_rotation(root)
        
        return root
    
    def search_id(self, root, id):
        if not root:
            return root
        if id<root.data.id:
            return self.search_id(root.left, id)
        if id>root.data.id:
            return self.search_id(root.right, id)
        return root
    
    def find_successor(self, root):
        if not root.right:
            return None
        ri = root.right
        while(ri.left):
            ri = ri.left
        return ri

    def delete(self, root, data):
        if not root:
            return root
        if self.comparator(root.data, data)==0:
            if not root.left:
                temp = root.right
                root = None
                return temp
            if not root.right:
                temp = root.left
                root = None
                return temp

            succ = self.find_successor(root)

            root.data = succ.data
            root.right = self.delete(root.right, succ.data)                

        elif self.comparator(root.data, data)==-1:
            root.right = self.delete(root.right, data)
        else:
            root.left = self.delete(root.left, data)
        
        root.height = 1+max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance<-1:
            bal2 = self.get_balance(root.right)
            if bal2<=0:
                return self.left_rotation(root)
            else:
                root.right = self.right_rotation(root.right)
                return self.left_rotation(root)
        
        if balance>1:
            bal2 = self.get_balance(root.left)
            if bal2>=0:
                return self.right_rotation(root)
            else:
                root.left = self.left_rotation(root.left)
                return self.right_rotation(root)

        
        return root
