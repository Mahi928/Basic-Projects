# Basic-Projects
This is the repository which contains some basic projects that includes implementation of data structures to solve real world problems.

# ✈️ Flight Planner
A Python-based flight route planner that determines optimal paths between cities based on various criteria like cost, number of flights, and travel time.

## 📁 Project Structure
### flight.py
Defines the Flight class to represent flight data.

Flight(
    flight_no: int,
    start_city: int,
    departure_time: int,
    end_city: int,
    arrival_time: int,
    fare: int
)
Each flight has a unique ID, departure and arrival cities, times, and fare. Cities and times are modeled as integers.

### planner.py
Implements the core route planning logic with three main methods:

🔹 least_flights_earliest_route(start, end, t1, t2)
Finds a valid path with:
<ul>
<li>the least number of flights, and</li>
<li>among them, the earliest arrival.</li>
</ul>
Uses BFS with a custom queue.

🔹 cheapest_route(start, end, t1, t2)
Finds the cheapest route within the time window.

Uses a min-heap (Dijkstra-like) algorithm.

🔹 least_flights_cheapest_route(start, end, t1, t2)
Finds a route with:
<ul>
<li>the least number of flights, and</li>
<li>among them, the lowest fare.</li>
</ul>
Uses a priority queue with (flight_count, fare) as priority.

Helper Classes
<ul>
<li>Heap: Custom min-heap for priority queue logic.</li>
<li>Queue: Simple FIFO queue for BFS.</li>
</ul>
### main.py
Sets up example flights, initializes the planner, and runs all three planning methods.

Demonstrates:

Usage of each planner method.
Comparison with expected outputs for validation.

✅ Example Task Goals
Task	Objective
1	Least flights, earliest arrival
2	Cheapest route
3	Least flights, among them the cheapest

## 🚀 How to Run
python main.py
