"""
CodingQuest Problem 29: Broken firewall

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
internal_bytes = 0
passenger_bytes = 0

for line in data:
    if not line:
        continue

    length_hex = line[4:8]
    packet_length = int(length_hex, 16)

    src_hex = line[24:28].lower()
    dest_hex = line[32:36].lower()

    is_internal = (src_hex == "c0a8" or dest_hex == "c0a8")
    is_passenger = (src_hex == "0a00" or dest_hex == "0a00")

    if is_internal:
        internal_bytes += packet_length
    if is_passenger:
        passenger_bytes += packet_length

ratio_string = f"{internal_bytes}/{passenger_bytes}"

print("Internal Systems Total Bytes:", internal_bytes)
print("Passenger Wifi Total Bytes:", passenger_bytes)
print("Verification Answer:", ratio_string)