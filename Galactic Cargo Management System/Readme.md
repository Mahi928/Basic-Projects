# Galactic Cargo Management System (GCMS)

This project is part of **COL106 Assignment 2** and implements an efficient bin-packing system used in interstellar cargo logistics. The **Galactic Cargo Management System (GCMS)** is designed to manage cargo items with varying sizes and colors into bins of fixed capacities using different allocation strategies based on cargo color.

## 🚀 Problem Background

In a futuristic setting, space cargo needs to be efficiently packed into bins aboard starships. Each bin has a capacity, and each cargo item has a size, color, and unique ID. The color of the cargo determines how it should be packed using specific fitting algorithms:

- 🔵 **Blue**: Compact Fit, choose bin with **smallest** sufficient capacity, **least ID**
- 🟡 **Yellow**: Compact Fit, choose bin with **smallest** sufficient capacity, **greatest ID**
- 🔴 **Red**: Largest Fit, choose bin with **largest** capacity, **least ID**
- 🟢 **Green**: Largest Fit, choose bin with **largest** capacity, **greatest ID**

## ⚙️ Features

- Add and remove bins and cargo objects
- Auto-assign objects to appropriate bins using specified strategies
- Retrieve information about bins and objects
- Raise exceptions when no suitable bin is available
- Efficient performance with `O(log(n) + log(m))` time complexity using custom AVL Trees

## 📁 File Descriptions

| File | Purpose |
|------|---------|
| `gcms.py` | Main interface for the cargo management system. Implements methods like `add_bin`, `add_object`, `delete_object`, `object_info`, and `bin_info`. |
| `bin.py` | Defines the `Bin` class, encapsulating bin ID, capacity, and stored objects. |
| `object.py` | Defines the `Object` class containing object ID, size, and color. |
| `avl.py` | Custom implementation of AVL Trees used for efficient lookup, insertion, and deletion of bins and objects based on custom comparison logic. |
| `node.py` | Contains the structure and utility functions for AVL tree nodes. |
| `exceptions.py` | Defines custom exceptions like `NoBinFoundException`. **(Do not modify)** |
| `main.py` | Sample script to test and debug the system manually. Not required for grading. |

## 📥 Sample Usage

```python
from gcms import GCMS
from object import Color

gcms = GCMS()

gcms.add_bin(101, 50)
gcms.add_bin(102, 60)

gcms.add_object(2001, 30, Color.RED)
gcms.add_object(2002, 20, Color.YELLOW)

print(gcms.object_info(2001))     # Might print 102
print(gcms.bin_info(102))        # (Remaining capacity, List of object IDs)

gcms.delete_object(2002)
