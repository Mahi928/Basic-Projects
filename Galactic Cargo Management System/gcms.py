from bin import Bin
from avl import AVLTree
from object import Object, Color
from exceptions import NoBinFoundException

def comp(node1, node2):
    if (node1.capacity, node1.id)>(node2.capacity, node2.id):
        return 1
    if (node1.capacity, node1.id)<(node2.capacity, node2.id):
        return -1
    return 0

def comp2(node1, node2):
    if (node1.capacity, node2.id)>(node2.capacity, node1.id):
        return 1
    if (node1.capacity, node2.id)<(node2.capacity, node1.id):
        return -1
    return 0

class GCMS:
    def __init__(self):
        # Maintain all the Bins and Objects in GCMS
        self._bins = AVLTree(comp)
        self._objects = AVLTree()
        self._bins_for_info = AVLTree()
        self._bins_RY = AVLTree(comp2)
        pass 

    def add_bin(self, bin_id, capacity):
        temp = Bin(bin_id, capacity)
        temp.objects = AVLTree()
        self._bins.root = self._bins.insert(self._bins.root, temp)
        self._bins_RY.root = self._bins_RY.insert(self._bins_RY.root, temp)
        self._bins_for_info.root = self._bins_for_info.insert(self._bins_for_info.root, temp)
        pass

    def add_object(self, object_id, size, color):
        obj = Object(object_id, size, color)
        temp = self._bins.root
        ans = temp
        if not temp:
            raise NoBinFoundException
        
            

        if(color==Color.BLUE):
            ans = temp
            while True:
                if(temp.left and temp.data.capacity>=size):
                    temp = temp.left
                elif(temp.right and temp.data.capacity<size):
                    temp = temp.right
                else:
                    break
                if(temp.data.capacity>=size):
                    ans = temp

        elif(color == Color.GREEN):
            while(temp.right):
                temp = temp.right
            ans = temp

        elif color==Color.RED:
            temp = self._bins_RY.root
            while(temp.right):
                temp=temp.right
            ans = temp

        elif color==Color.YELLOW:
            temp = self._bins_RY.root
            ans = temp
            while True:
                if(temp.left and temp.data.capacity>=size):
                    temp = temp.left
                elif(temp.right and temp.data.capacity<size):
                    temp = temp.right
                else: break
                if(temp.data.capacity>=size):
                    ans = temp
        
        temp = ans

        if temp.data.capacity<size :
                raise NoBinFoundException
        
        # print(self._bins_RY.traverse(self._bins_RY.root, []))
        req_bin = temp.data
        self._bins.root = self._bins.delete(self._bins.root, req_bin)
        self._bins_RY.root = self._bins_RY.delete(self._bins_RY.root, req_bin)
        req_bin.add_object(obj)
        self._bins.root = self._bins.insert(self._bins.root, req_bin)
        self._bins_RY.root = self._bins_RY.insert(self._bins_RY.root, req_bin)
        self._objects.root = self._objects.insert(self._objects.root, obj)
        # print(self._bins_RY.traverse(self._bins_RY.root, []))

            

    def delete_object(self, object_id):
        # Implement logic to remove an object from its bin
        binid = self.object_info(object_id)
        if binid == None: return
        temp1 = self._bins_for_info.search_id(self._bins_for_info.root, binid).data
        object = temp1.objects.search_id(temp1.objects.root, object_id).data
        req_bin = temp1
        self._bins.root = self._bins.delete(self._bins.root, req_bin)
        self._bins_RY.root = self._bins_RY.delete(self._bins_RY.root, req_bin)
        temp1.remove_object(object_id)
        self._bins.root = self._bins.insert(self._bins.root, req_bin)
        self._bins_RY.root = self._bins_RY.insert(self._bins_RY.root, req_bin)
        self._objects.root = self._objects.delete(self._objects.root, object)
        pass

    def bin_info(self, bin_id):
        # returns a tuple with current capacity of the bin and the list of objects in the bin (int, list[int])
        temp = self._bins_for_info.search_id(self._bins_for_info.root, bin_id).data
        lis = temp.objects.traverse(temp.objects.root, [])
        return (temp.capacity, lis)
        pass

    def object_info(self, object_id):
        # returns the bin_id in which the object is stored
        temp = self._objects.search_id(self._objects.root, object_id)
        if temp:
            return temp.data.bin_id
        return None
        pass

    
    