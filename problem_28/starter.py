"""
CodingQuest Problem 28: Purchase tickets

Your input data is in input.txt.
The data has been loaded into a list called `data` for you.
Each item in the list is one line from the file, as a string.

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

company_totals = defaultdict(int)
subtractions = {"discount", "rebate"}

for line in data:
    if not line:
        continue

    parts = line.split(":", 1)
    if len(parts) < 2:
        continue

    company = parts[0].strip()
    action_and_val = parts[1].split()

    if len(action_and_val) == 2:
        action = action_and_val[0].lower()
        amount = int(action_and_val[1])

        if action in subtractions:
            company_totals[company] -= amount
        else:
            company_totals[company] += amount

cheapest_price = min(company_totals.values())

print("Cheapest Ticket Option:", cheapest_price)
