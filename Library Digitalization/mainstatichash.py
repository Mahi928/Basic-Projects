import time
import random
import string
from hash_table import HashSet, HashMap
from prime_generator import set_primes

# Set the prime sizes for the hash tables
prime_sizes = [1010, 103, 107, 109, 11301]
set_primes(prime_sizes)

# Parameters for hashing
z = 31  # Parameter for polynomial accumulation
z1, z2, c2 = 31, 37, 1733#1733  # Parameters for double hashing
initial_table_size = 2053  #2053# Initial table size

# Initialize HashMap and HashSet for different collision resolution methods
params_chain = (z, initial_table_size)
params_linear = (z, initial_table_size)
params_double = (z1, z2, c2, initial_table_size)

hashmap_chain = HashMap("Chain", params_chain)
hashmap_linear = HashMap("Linear", params_linear)
hashmap_double = HashMap("Double", params_double)

hashset_chain = HashSet("Chain", params_chain)
hashset_linear = HashSet("Linear", params_linear)
hashset_double = HashSet("Double", params_double)

# Built-in Python dict and set
python_dict = {}
python_set = set()

# Number of elements
n = initial_table_size
num_elements = n# change this to change number of keys inserted 

# Function to generate random string
random.seed(42)  # Fix randomness
def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

# Generate sample data
key_length = 2
value_length = 4
keys = []
values = []

while len(keys) < num_elements:
    key = generate_random_string(key_length)
    if key not in python_set:
        python_set.add(key)
        keys.append(key)
        values.append(generate_random_string(value_length))

# Measure and insert into HashMaps
start_time = time.time()
for i in range(num_elements):
    key, value = keys[i], values[i]
    hashmap_chain.insert((key, value))
    hashmap_linear.insert((key, value))
    hashmap_double.insert((key, value))
    python_dict[key] = value



# Measure and insert into HashSets

for key in keys:
    hashset_chain.insert(key)
    hashset_linear.insert(key)
    hashset_double.insert(key)



# Print Load Factors
def print_loads():
    print(f"HashMap (Chain) Load Factor: {hashmap_chain.get_load():.3f}")
    print(f"HashMap (Linear) Load Factor: {hashmap_linear.get_load():.3f}")
    print(f"HashMap (Double) Load Factor: {hashmap_double.get_load():.3f}")
    print(f"HashSet (Chain) Load Factor: {hashset_chain.get_load():.3f}")
    print(f"HashSet (Linear) Load Factor: {hashset_linear.get_load():.3f}")
    print(f"HashSet (Double) Load Factor: {hashset_double.get_load():.3f}")

print_loads()

# Functions to check consistency
def check_maps(hashmap, python_map):
    for key in python_map:
        custom_value = hashmap.find(key)
        python_value = python_map[key]
        if custom_value != python_value:
            print(f"Mismatch for key {key}: Custom {custom_value}, Python {python_value}")
            return False
    print("HashMap matches Python dict!")
    return True

def check_sets(hashset, python_set):
    for key in python_set:
        if not hashset.find(key):
            print(f"Key {key} missing in custom HashSet!")
            return False
    print("HashSet matches Python set!")
    return True

# Check consistency and print results
print("Checking HashMap (Chain)...")
check_maps(hashmap_chain, python_dict)

print("Checking HashMap (Linear)...")
check_maps(hashmap_linear, python_dict)

print("Checking HashMap (Double)...")
check_maps(hashmap_double, python_dict)

print("Checking HashSet (Chain)...")
check_sets(hashset_chain, python_set)

print("Checking HashSet (Linear)...")
check_sets(hashset_linear, python_set)

print("Checking HashSet (Double)...")
check_sets(hashset_double, python_set)

end_time = time.time()
print(f"Time for HashMap : {end_time - start_time:.3f} seconds")
#print(str(hashset_double))
#print(str(hashmap_double))
