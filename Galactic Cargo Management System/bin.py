class Bin:
    def __init__(self, bin_id, capacity):
        self.id = bin_id
        self.capacity = capacity
        self.objects = None
        pass

    def add_object(self, object):
        # Implement logic to add an object to this bin
        object.bin_id = self.id
        self.capacity-=object.size
        self.objects.root = self.objects.insert(self.objects.root, object)
        pass

    def remove_object(self, object_id):
        # Implement logic to remove an object by ID
        object = self.objects.search_id(self.objects.root, object_id).data
        self.capacity += object.size
        self.objects.root = self.objects.delete(self.objects.root, object)
        pass
