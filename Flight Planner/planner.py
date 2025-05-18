from flight import Flight

class Planner:
    def __init__(self, flights):
        """The Planner

        Args:
            flights (List[Flight]): A list of information of all the flights (objects of class Flight)
        """
        self.flights = flights
        self.no_of_cities = 0
        for flight in flights:
            self.no_of_cities = max([self.no_of_cities, flight.start_city, flight.end_city])
        
        self.no_of_cities += 1
        self.graph = [[] for _ in range(self.no_of_cities)]
        for flight in flights:
            self.graph[flight.start_city].append(flight)
        pass
    
    def least_flights_earliest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route has the least number of flights, and within routes with same number of flights, 
        arrives the earliest
        """
        if start_city == end_city:
            return []

        vis = [0]*(len(self.flights)+1)
        arr = [None]*(len(self.flights)+1)

        q = Queue()
        last_flight = None
        min_time = float("inf")

        for flight in self.graph[start_city]:
            if flight.arrival_time <= t2 and flight.departure_time >= t1 and not vis[flight.flight_no]:
                vis[flight.flight_no] = 1
                q.enqueue(flight)
                if flight.end_city == end_city and flight.arrival_time < min_time:
                    last_flight = flight
                    min_time = flight.arrival_time

        if last_flight:
            return [last_flight]

        while q.size():
            k = q.size()
            while k:
                k-=1
                prev_flight = q.dequeue()
                for flight in self.graph[prev_flight.end_city]:
                    if flight.departure_time>=prev_flight.arrival_time+20 and flight.arrival_time <= t2 and not vis[flight.flight_no]:
                        vis[flight.flight_no] = 1
                        q.enqueue(flight)
                        arr[flight.flight_no] = prev_flight
                        if flight.end_city == end_city and flight.arrival_time < min_time:
                            last_flight = flight
                            min_time = flight.arrival_time
            
            if last_flight:
                break
        ans = []
        if not last_flight:
            return []
        while last_flight.start_city != start_city:
            ans.append(last_flight)
            last_flight = arr[last_flight.flight_no]

        ans.append(last_flight)
        ans.reverse()
        return ans

    def cheapest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route is a cheapest route
        """
        if start_city == end_city:
            return []
        vis = [0]*(len(self.flights)+1)
        arr = [None]*(len(self.flights)+1)
        
        last_flight = None
        pq = Heap(lambda x, y: x[0]<=y[0], [])
        for flight in self.graph[start_city]:
            ele = (flight.fare, flight)
            if flight.departure_time>=t1 and flight.arrival_time<=t2 and not vis[flight.flight_no]:
                vis[flight.flight_no] = 1
                pq.insert(ele)
        
        while pq.top():
            min_route = pq.extract()
            fare = min_route[0]
            prev_flight = min_route[1]
            if prev_flight.end_city == end_city:
                last_flight = prev_flight
                break
            for flight in self.graph[prev_flight.end_city]:
                if flight.departure_time >= prev_flight.arrival_time+20 and not vis[flight.flight_no] and flight.arrival_time<=t2:
                    vis[flight.flight_no] = 1
                    arr[flight.flight_no] = prev_flight
                    pq.insert((fare+flight.fare, flight))

        if not last_flight:
            return []
        ans = []
        while last_flight.start_city!=start_city:
            ans.append(last_flight)
            last_flight = arr[last_flight.flight_no]
        ans.append(last_flight)

        ans.reverse()
        return ans
        pass

    
    def least_flights_cheapest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route has the least number of flights, and within routes with same number of flights, 
        is the cheapest
        """
        if start_city == end_city:
            return []
        vis = [0]*(len(self.flights)+1)
        arr = [None]*(len(self.flights)+1)
        
        last_flight = None
        pq = Heap(lambda x, y: x[0]<=y[0], [])
        for flight in self.graph[start_city]:
            ele = ((1, flight.fare), flight)
            if flight.departure_time>=t1 and flight.arrival_time<=t2 and not vis[flight.flight_no]:
                vis[flight.flight_no] = 1
                pq.insert(ele)
        
        while pq.top():
            ele = pq.extract()
            tup = ele[0]
            fare = tup[1]
            step = tup[0]
            prev_flight = ele[1]
            if prev_flight.end_city == end_city:
                last_flight = prev_flight
                break
            for flight in self.graph[prev_flight.end_city]:
                if flight.departure_time >= prev_flight.arrival_time+20 and not vis[flight.flight_no] and flight.arrival_time<=t2:
                    vis[flight.flight_no] = 1
                    arr[flight.flight_no] = prev_flight
                    pq.insert(((step+1, fare+flight.fare), flight))

        if not last_flight:
            return []
        ans = []
        while last_flight.start_city!=start_city:
            ans.append(last_flight)
            last_flight = arr[last_flight.flight_no]
        ans.append(last_flight)

        ans.reverse()
        return ans
                    
        pass


class Heap:
    def __init__(self, comparison_function, init_array):
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
        child = left_child
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
        self.arr.append(value)
        child = len(self.arr)-1
        self.upheap(child)
        pass
    
    def extract(self):
        if len(self.arr)==0: return None
        ans = self.arr[0]
        self.arr[0] = self.arr[-1]
        self.arr.pop()
        self.downheap(0)
        return ans
        pass
    
    def top(self):
        if len(self.arr)==0: return None
        return self.arr[0]
        pass

    def size(self):
        return len(self.arr)



class Queue:
    def __init__(self):
        self.arr = []
        self.f = 0
        self.r = -1
        pass

    def enqueue(self, ele):
        self.arr.append(ele)
        self.r+=1
    
    def dequeue(self):
        if self.r<self.f:
            return None
        
        ele = self.arr[self.f]
        self.f+=1
        return ele
    
    def size(self):
        return self.r-self.f+1
        