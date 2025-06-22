# ✈️ Flight Planner

Flight Planner is a Python-based flight route planner that leverages advanced data structures and graph algorithms to efficiently compute the cheapest, fastest, and most optimal flight routes between cities. Designed for scalability, it handles layovers, exchanges, and large datasets with ease.

---

## 📦 Project Structure

- [flight.py](flight.py)  
  Defines the Flight class, representing each flight with a unique ID, departure/arrival cities, times, and fare.

- [planner.py](planner.py)  
  Implements the core route planning logic using advanced graph algorithms:
  - least_flights_earliest_route(start, end, t1, t2)  
    Finds a path with the fewest flights and, among those, the earliest arrival (BFS with custom queue).
  - cheapest_route(start, end, t1, t2)  
    Finds the lowest-cost route within the time window (Dijkstra-like with custom min-heap).
  - least_flights_cheapest_route(start, end, t1, t2)  
    Finds the route with the fewest flights and, among those, the lowest fare (priority queue by (flight_count, fare)).

  Helper Classes:  
  - Heap: Custom min-heap for efficient priority queue operations.  
  - Queue: Simple FIFO queue for BFS traversal.

- [main.py](main.py)  
  Demonstrates usage: sets up sample flights, initializes the planner, and runs all three planning methods with validation.

---

## ✅ Example Tasks

| Task | Objective                              |
|------|----------------------------------------|
|  1   | Least flights, earliest arrival        |
|  2   | Cheapest route                        |
|  3   | Least flights, among them the cheapest|

---

## 🚀 Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/Mahi928/Basic-Projects.git
   cd Flight Planner
   
1. Run the example:
  
   python main.py
   
---

## 🛠️ Features

- Advanced graph algorithms for optimal route planning
- Custom data structures for performance and scalability
- Handles layovers, exchanges, and time/fare constraints
- Easy to extend for real-world datasets

---
