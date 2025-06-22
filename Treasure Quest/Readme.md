# 🏴‍☠️ Treasure Quest: The Straw Hat Crew!

## Overview

This project models a treasure management and scheduling system inspired by the adventures of the Straw Hat pirates from *One Piece*. Each crewmate processes treasure piles arriving at different times and sizes. The goal is to implement a system that assigns and processes treasure efficiently using custom-built data structures.

The project simulates the task as a **multi-agent scheduling problem**, where treasure is assigned based on load balancing and processed based on priority.

---

## 🧠 Problem Model

- **Crewmates (m):** Workers who manage treasures one at a time.
- **Treasure:** Each has a unique ID, size (time to process), and arrival time.
- **Load:** Defined as the total remaining size of treasures for each crewmate.
- **Priority:** Calculated as `WaitTime - RemainingSize`, determining the next treasure to be processed.

---

## 🗂 File Descriptions

### `heap.py`
Implements a **generic min-heap** from scratch using any comparison function.
- `__init__`: O(n) heap construction.
- `insert`: O(log n) insertion.
- `extract`: O(log n) removal of the top element.
- `top`: O(1) access to the top element.

### `crewmate.py`
Defines the `Crewmate` class representing each crew member.
- Stores assigned treasures and their remaining processing loads.
- Provides treasure selection based on load and priority rules.

### `straw_hat.py`
Implements the main controller class `StrawHatTreasury`.
- `__init__(m)`: Initializes system with `m` crewmates.
- `add_treasure(...)`: Assigns incoming treasure to least-loaded crewmate and updates system state.
- `get_completion_time()`: Returns list of all treasures with their computed completion times, sorted by ID.

### `treasure.py`
Defines the `Treasure` class.
- Stores treasure ID, size, arrival time, and completion time.
- The class constructor must remain unchanged as per assignment constraints.

### `custom.py`
Optional utility file.
- You can define additional helper functions or classes here to support your implementation.
- No constraints on how many functions or classes can be written, as long as starter code interfaces remain unchanged.

---

## ⚙️ How to Run

Follow these steps to run the code locally:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Mahi928/Basic-Projects.git
   cd Treasure Quest
2. **Ensure Python 3 is installed** on your system.
3. **Run your test file or write your own test script** that uses the StrawHatTreasury class and invokes its methods.
   ## Example Test Structure:
   ```python
   from straw_hat import StrawHatTreasury
   from treasure import Treasure
   
   treasury = StrawHatTreasury(m=3)
   treasury.add_treasure(Treasure(id=1, size=5, arrival=1))
   treasury.add_treasure(Treasure(id=2, size=3, arrival=2))
   result = treasury.get_completion_time()
   for treasure in result:
       print(treasure.id, treasure.completion_time)
