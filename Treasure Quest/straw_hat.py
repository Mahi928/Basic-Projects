'''
    This file contains the class definition for the StrawHat class.
'''

import crewmate
import heap
import treasure

class StrawHatTreasury:
    '''
    Class to implement the StrawHat Crew Treasury
    '''
    
    def __init__(self, m):
        '''
        Arguments:
            m : int : Number of Crew Mates (positive integer)
        Returns:
            None
        Description:
            Initializes the StrawHat
        Time Complexity:
            O(m)
        '''
        
        # Write your code here
        self.m = m
        self.crew_arr = heap.Heap(self.comp, [crewmate.CrewMate(i) for i in range(m)])
        self.managing_team = []
        self.treasures = []
        pass
    
    def add_treasure(self, treasure):
        '''
        Arguments:
            treasure : Treasure : The treasure to be added to the treasury
        Returns:
            None
        Description:
            Adds the treasure to the treasury
        Time Complexity:
            O(log(m) + log(n)) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        # Write your code here
        treasure.assign()
        arrival = treasure.arrival_time
        mn = self.crew_arr.extract()
        if arrival>=mn.load:
            mn.load = arrival + treasure.size
        else:
            mn.load += treasure.size
        mn.add_treasure(treasure)
        self.crew_arr.insert(mn)
        self.managing_team.append(mn)
        self.treasures.append(treasure)
        pass
    
    def get_completion_time(self):
        '''
        Arguments:
            None
        Returns:
            List[Treasure] : List of treasures in the order of their completion after updating Treasure.completion_time
        Description:
            Returns all the treasure after processing them
        Time Complexity:
            O(n(log(m) + log(n))) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        
        # Write your code here
        n = len(self.treasures)
        if self.m<n:
            crews = []
            while self.crew_arr.top():
                crew = self.crew_arr.extract()
                crew.treasures_heap = heap.Heap(self.comp2, [])
                crews.append(crew)
                l = crew.treasures
                for i in range(len(l)):
                    time = l[i].arrival_time - crew.prev
                    temp = crew.prev
                    while time>0 and crew.treasures_heap.top():
                        treas = crew.treasures_heap.extract()
                        if time>=treas.remaining_size:
                            time -= treas.remaining_size
                            treas.completion_time = temp + treas.remaining_size
                            temp = treas.completion_time
                        else:
                            treas.remaining_size -= time
                            time = 0
                            crew.treasures_heap.insert(treas)

                    crew.treasures_heap.insert(l[i])
                    crew.prev = l[i].arrival_time
                    
                crew.extra_time = crew.prev
                while crew.treasures_heap.top():
                    treas = crew.treasures_heap.extract()
                    treas.completion_time = treas.remaining_size + crew.extra_time
                    crew.extra_time = treas.completion_time
                
            for crew in crews:
                self.crew_arr.insert(crew)
        else:
            for crew in self.managing_team:
                crew.treasures_heap = heap.Heap(self.comp2, [])
                l = crew.treasures
                for i in range(len(l)):
                    time = l[i].arrival_time - crew.prev
                    temp = crew.prev
                    while time>0 and crew.treasures_heap.top():
                        treas = crew.treasures_heap.extract()
                        if time>=treas.remaining_size:
                            time -= treas.remaining_size
                            treas.completion_time = temp + treas.remaining_size
                            temp = treas.completion_time
                        else:
                            treas.remaining_size -= time
                            time = 0
                            crew.treasures_heap.insert(treas)

                    crew.treasures_heap.insert(l[i])
                    crew.prev = l[i].arrival_time
                    
                crew.extra_time = crew.prev
                while crew.treasures_heap.top():
                    treas = crew.treasures_heap.extract()
                    treas.completion_time = treas.remaining_size + crew.extra_time
                    crew.extra_time = treas.completion_time

        for tres in self.treasures:
            tres.assign()
        self.treasures.sort(key= lambda x:x.id)
        return self.treasures

        pass
    
    # You can add more methods if required
    def comp(self, crew1, crew2):
        return crew1.load<crew2.load
    
    def comp2(self, treas1, treas2):
        return ((treas1.arrival_time+treas1.remaining_size, treas1.id)<(treas2.arrival_time+treas2.remaining_size, treas2.id))
    
    def rev_comp(self, crew1, crew2):
        return crew1.load>crew2.load