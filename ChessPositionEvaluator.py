import argparse

alpha_to_numeric = {
    "a" : 1,
    "b" : 2,
    "c" : 3,
    "d" : 4,
    "e" : 5,
    "f" : 6,
    "g" : 7,
    "h" : 8
}

numeric_to_alpha = {
    1: "a",
    2: "b",
    3: "c",
    4: "d",
    5: "e",
    6: "f",
    7: "g",
    8: "h"
}


def all_valid_moves(potential_positions):
    # Return all valid positions in alphanumeric format
    potential_moves = []
    for i in potential_positions:
        potential_moves.append("".join([numeric_to_alpha[i[1]], str(i[0])]))
    return potential_moves


def get_straight_moves(x, y):
    # Return all possible vertical and horizontal positions
    straight_moves = []
    up = [(x, y + i) for i in range(1, 8) if 1 <= y + i <= 8]
    down = [(x, y - i) for i in range(1, 8) if 1 <= y - i <= 8]
    left = [(x - i, y) for i in range(1, 8) if 1 <= x - i <= 8]
    right = [(x + i, y) for i in range(1, 8) if 1 <= x + i <= 8]
    straight_moves += up + down + left + right
    return straight_moves


def get_cross_moves(x, y):
    # Return all possible cross positions
    cross_moves = []
    upright = [(x + i, y + i) for i in range(1, 8) if (1 <= x + i <= 8) and (1 <= y + i <= 8)]
    downright = [(x - i, y + i) for i in range(1, 8) if (1 <= x - i <= 8) and (1 <= y + i <= 8)]
    upleft = [(x + i, y - i) for i in range(1, 8) if (1 <= x + i <= 8) and (1 <= y - i <= 8)]
    downleft = [(x - i, y - i) for i in range(1, 8) if (1 <= x - i <= 8) and (1 <= y - i <= 8)]
    cross_moves += upright + downright + upleft + downleft
    return cross_moves


def find_knight_moves(position):
    # Return all potential positions for a knight from a given "position"
    potential_positions = []
    column, row = list(position.strip())
    column = alpha_to_numeric[column]
    x, y = int(row), int(column)
    if (1 <= x + 2 <= 8) and (1 <= y + 1 <= 8):
        potential_positions.append([x + 2, y + 1])
    if (1 <= x + 1 <= 8) and (1 <= y + 2 <= 8):
        potential_positions.append([x + 1, y + 2])
    if (1 <= x - 1 <= 8) and (1 <= y + 2 <= 8):
        potential_positions.append([x - 1, y + 2])
    if (1 <= x - 2 <= 8) and (1 <= y + 1 <= 8):
        potential_positions.append([x - 2, y + 1])
    if (1 <= x - 2 <= 8) and (1 <= y - 1 <= 8):
        potential_positions.append([x - 2, y - 1])
    if (1 <= x - 1 <= 8) and (1 <= y - 2 <= 8):
        potential_positions.append([x - 1, y - 2])
    if (1 <= x + 1 <= 8) and (1 <= y - 2 <= 8):
        potential_positions.append([x + 1, y - 2])
    if (1 <= x + 2 <= 8) and (1 <= y - 1 <= 8):
        potential_positions.append([x + 2, y - 1])

    potential_moves = all_valid_moves(potential_positions)
    return potential_moves


def find_rook_moves(position):
    # Return all potential positions for a rook from a given "position"
    column, row = list(position.strip())
    column = alpha_to_numeric[column]
    x, y = int(row), int(column)
    potential_positions = get_straight_moves(x, y)
    potential_moves = all_valid_moves(potential_positions)
    return potential_moves


def find_bishop_moves(position):
    # Return all potential positions for a bishop from a given "position"
    column, row = list(position.strip())
    column = alpha_to_numeric[column]
    x, y = int(row), int(column)
    potential_positions = get_cross_moves(x, y)
    potential_moves = all_valid_moves(potential_positions)
    return potential_moves


def find_queen_moves(position):
    # Return all potential positions for a queen from a given "position"
    potential_positions = []
    column, row = list(position.strip())
    column = alpha_to_numeric[column]
    x, y = int(row), int(column)
    potential_cross_positions = get_cross_moves(x, y)
    potential_straight_positions = get_straight_moves(x, y)
    potential_positions += potential_straight_positions + potential_cross_positions
    potential_moves = all_valid_moves(potential_positions)
    return potential_moves


# Parse input arguments
parser = argparse.ArgumentParser()
parser.add_argument("-piece", help="Chess piece : e.g. rook, knight, bishop, queen", required=True)
parser.add_argument("-position", help="Current position of the chess piece: e.g. E4, D6 etc", required=True)
args = parser.parse_args()

# Convert piece name and position to lower case
piece = args.piece.strip().lower()
position = args.position.strip().lower()

# Check the chess piece provided as input and call the relevant function to get the possible board positions for it.
if piece == "knight":
    potential_board_positions = find_knight_moves(position)
    print("Piece:", piece)
    print("Current Position:", position)
    print("Potential Board Positions are:", potential_board_positions)
elif piece == "rook":
    potential_board_positions = find_rook_moves(position)
    print("Piece:", piece)
    print("Current Position:", position)
    print("Potential Board Positions are:", potential_board_positions)
elif piece == "bishop":
    potential_board_positions = find_bishop_moves(position)
    print("Piece:", piece)
    print("Current Position:", position)
    print("Potential Board Positions are:", potential_board_positions)
elif piece == "queen":
    potential_board_positions = find_queen_moves(position)
    print("Piece:", piece)
    print("Current Position:", position)
    print("Potential Board Positions are:", potential_board_positions)
else:
    print("Please enter knight, rook, bishop or queen only")