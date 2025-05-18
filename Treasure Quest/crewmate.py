'''
    Python file to implement the class CrewMate
'''

class CrewMate:
    '''
    Class to implement a crewmate
    '''
    
    def __init__(self, load=0):
        '''
        Arguments:
            None
        Returns:
            None
        Description:
            Initializes the crewmate
        '''
        
        # Write your code here
        self.load = load
        self.treasures = []
        self.extra_time = 0
        self.prev = 0
        self.treasures_heap = None
        pass
    
    # Add more methods if required
    def add_treasure(self, treasure):
        self.treasures.append(treasure)