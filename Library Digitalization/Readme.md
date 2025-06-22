# 📚 Library Digitalization Project

## 📝 Overview

The **Library Digitalization** project aims to modernize the IITD Library by enabling searchable, compressed dictionaries for each book. It provides functionalities to:

- Extract **distinct words** from a book
- Search for **books containing a specific keyword**
- **Compare different hashing strategies** and sorting-based techniques for word extraction

Two main approaches are used:

1. **Sorting-Based Approach (MuskLibrary)** using MergeSort
2. **Hash-Based Approach (JGBLibrary)** with different collision resolution methods: Chaining, Linear Probing, and Double Hashing

---

## 📂 Project Structure

### 1. `hash_table.py`

Implements hash table data structures used in the JGBLibrary approach.

#### Key Components:

- **`HashTable` (Base class)**: Shared logic for `HashSet` and `HashMap`
- **`HashSet`**: Stores only unique keys
- **`HashMap`**: Stores key-value pairs (only key is hashed)

#### Collision Handling Methods:

- `Chain`: Uses lists to handle collisions
- `Linear`: Probes linearly to find the next available slot
- `Double`: Uses a second hash function to calculate the probing step

---

### 2. `dynamic hash table.py`

Extends `hash_table.py` to handle dynamic resizing of hash tables for better space efficiency.

#### Key Features:

- **`DynamicHashSet` and `DynamicHashMap`**:
  - Automatically **rehash** when load factor exceeds 50%
  - Use `get_next_size()` from `prime_generator.py` to get the new table size

- Rehashing preserves data while adapting table size for optimized performance

---

### 3. `library.py`

Defines the core logic for the Digital Library.

#### Classes:

- **`DigitalLibrary`**: Abstract base class defining shared methods:
  - `distinct_words`
  - `count_distinct_words`
  - `search_keyword`
  - `print_books`

##### a. `MuskLibrary`

- Uses **MergeSort** to find distinct words
- Maintains **sorted order** of words
- All books are given at once during initialization

##### b. `JGBLibrary`

- Uses customized **HashTable-based methods** (Jobs, Gates, Bezos)
- Allows adding books **incrementally** via `add_book`
- Words stored in **insertion or hashing order**, not sorted

---

### 4. `prime generator.py`

Helper utility used for dynamic resizing.

- **Provides `get_next_size()`**: Returns the next prime number greater than twice the current size

---

### 5. `main.py`

- Entry point for testing the library functionalities
- Meant for **debugging and local validation**
- You can write sample books, try search, distinct words, and print functions here

---

## ✅ Functional Requirements

### Supported Operations:

- Extract **distinct words** from any book
- Count the number of distinct words
- Perform **keyword-based book search**
- Print the current collection in a structured format

### Constraints:

- No usage of Python built-in `set` or `dict`
- No third-party libraries — implement everything from scratch
- Must adhere to **expected time complexities** for grading

---

## 🧠 Strategies & Comparisons

| Strategy        | Dev Name | Method Used        | Collision Handling     |
|----------------|----------|--------------------|------------------------|
| MergeSort      | Musk     | Sorting             | N/A                    |
| Hashing        | Jobs     | HashMap / HashSet   | Chaining               |
| Hashing        | Gates    | HashMap / HashSet   | Linear Probing         |
| Hashing        | Bezos    | HashMap / HashSet   | Double Hashing         |

Each method has been implemented as a different configuration under the `JGBLibrary`.

---

## 🚀 How to Run

1. Place all files in the same directory
2. Use `main.py` to create instances of `MuskLibrary` or `JGBLibrary`
3. Add books and test functions like:
   - `distinct_words(book_title)`
   - `search_keyword(keyword)`
   - `print_books()`

---
