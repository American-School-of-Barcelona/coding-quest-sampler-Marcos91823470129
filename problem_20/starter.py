"""
CodingQuest Problem 20: Tic tac toe

Your input data is in input.txt.
The data has been loaded into a list called `data` for you.
Each item in the list is one line from the file, as a string.

Each line represents one game of tic-tac-toe.
The numbers on each line are the squares played, in order (X goes first).
Squares are numbered like this:

 1 | 2 | 3
---|---|---
 4 | 5 | 6
---|---|---
 7 | 8 | 9

Process each game until someone wins (3 in a row), then stop.
If nobody wins after 9 moves, it's a draw.

Your answer is: (games won by X) * (games won by O) * (drawn games)

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

winning_combinations = [
    {1, 2, 3}, {4, 5, 6}, {7, 8, 9},
    {1, 4, 7}, {2, 5, 8}, {3, 6, 9},
    {1, 5, 9}, {3, 5, 7}
]

x_wins = 0
o_wins = 0
draws = 0

for line in data:
    moves = [int(x) for x in line.split()]
    x_squares = set()
    o_squares = set()
    game_over = False

    for index, move in enumerate(moves):
        if index % 2==0:
            x_squares.add(move)
            for combo in winning_combinations:
                if combo.issubset(x_squares):
                    x_wins += 1
                    game_over = True
                    break

        else:
            o_squares.add(move)
            for combo in winning_combinations:
                if combo.issubset(o_squares):
                    o_wins += 1
                    game_over = True
                    break

        if game_over:
            break

    if not game_over:
        draws += 1

final_product = x_wins * o_wins * draws

print("X Wins:", x_wins)
print("O Wins:", o_wins)
print("Draws:", draws)
print("Verification Answer:", final_product)

