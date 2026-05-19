"""
CodingQuest Problem 18: Inventory check

Your input data is in input.txt.
The data has been loaded into a list called `data` for you.
Each item in the list is one line from the file, as a string.

Each line has three parts separated by spaces:
  - A unique item ID
  - A quantity (number)
  - A category name

Write your solution below the comment line.
"""

# --- Load the data (don't change this) ---
with open("input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

# Take a look at the first few lines
print(f"Loaded {len(data)} lines.")
print("First 5 lines:")
for line in data[:5]:
    print("  ", line)
print()

# --- Your code here ---
from collections import defaultdict
import math

with open("input.txt", "r") as f:
    data = [line.strip() for line in f.readlines()]

print(f"Loaded {len(data)} lines.")
print("First 5 lines:")
for line in data[:5]:
    print("  ", line)
print()

category_totals = defaultdict(int)

for line in data:
    parts = line.split()
    if len(parts) >= 3:
        quantity = int(parts[1])
        category = parts[2]
        category_totals[category] += quantity

mod_values = []
for total in category_totals.values():
    mod_values.append(total % 100)

verification_product = math.prod(mod_values)
print("Verification Answer", verification_product)