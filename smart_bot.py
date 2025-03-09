"""
smart_bot.py

This module implements the Smart Bot for a game, designed to determine the best move based on the current game board.

How it works:
1. Board Analysis: Identifies positions occupied by the bot and the opponent and calculates remaining possible moves.
2. Strategic Evaluation: Assigns priorities to moves that either maximize the bot's chances of winning or minimize the opponents chances of winning.
3. Move Prioritisation: Bot examines which direction (diagonal/vertical/horizontal) has the most stones and orders these moves in an ascending list
3. Move Optimization: Bot prefers diagonal over horizontal/vertical moves because a diagonal move has the same winning chances on an empty field as the hori/verti moves plus the diagnoal moves in addition
4. Take first Element: After ordering the moves based on how many stones are in the respective lines, the bot picks the first element of the list

Functions:
- get_player_fields(board, player_symbol): Extracts positions occupied by a player.
- get_possible_moves(board): Returns all available moves.
- get_diagonal_counts(board, player_symbol): Counts positions along diagonals for a player.
- get_horizontal_counts(board, player_symbol): Counts positions in rows.
- get_vertical_counts(board, player_symbol): Counts positions in columns.
- make_random_move(board): Selects a random valid move.
- calc_optimized_move(board, player_symbol): Calculates the most strategic move for a player.
- make_smart_move(board, player_symbol, opponent_symbol): Finds the best move while countering the opponent.

This modular design ensures adaptability and competitiveness.
"""

import random
from collections import defaultdict

def get_player_fields(game_board, player_symbol):
    """
    Extracts all fields occupied by a given player.

    Args:
        game_board (list): The current game board represented as a 2D list.
        player_symbol (str): The symbol of the player ('X' or 'O').

    Returns:
        list: A list of moves (1-9) occupied by the player.
    """
    # Extract all positions on the board that the player has occupied.
    elements = []
    prev_rows = 0
    for row_index in range(len(game_board)):
        for col_index in range(len(game_board[row_index])):
            if game_board[row_index][col_index] == player_symbol:
                # Convert the row and column indices into a move (1-9).
                move = row_index + prev_rows + col_index + 1
                elements.append(move)
        # Increment by 2 to account for previous rows.
        prev_rows += 2
    return elements

def get_possible_moves(game_board):
    """
    Computes all unoccupied fields on the game board.

    Args:
        game_board (list): The current game board represented as a 2D list.

    Returns:
        list: A list of possible moves (1-9) that are not occupied.
    """
    # Calculate the difference between all fields and the fields already occupied by both players.
    occupied_fields_other = get_player_fields(game_board, "X")
    occupied_fields_KI = get_player_fields(game_board, "O")
    occupied_fields_all = set(occupied_fields_other + occupied_fields_KI)

    all_fields = set(range(1, 10))  # All valid moves (1-9).
    possible_moves = all_fields.difference(occupied_fields_all)
    return list(possible_moves)

def get_diagonal_counts(game_board, player_symbol):
    """
    Counts the number of fields occupied by the player on both diagonals.

    Args:
        game_board (list): The current game board represented as a 2D list.
        player_symbol (str): The symbol of the player ('X' or 'O').

    Returns:
        dict: A dictionary with diagonal indices (0 and 1) as keys and counts as values.
    """
    # Count how many positions on the two main diagonals are occupied by the player.
    count_diag1 = 0  # Top-left to bottom-right diagonal.
    count_diag2 = 0  # Top-right to bottom-left diagonal.

    for i in range(3):
        if game_board[i][i] == player_symbol:
            count_diag1 += 1
        if game_board[i][2 - i] == player_symbol:
            count_diag2 += 1

    return {0: count_diag1, 1: count_diag2}

def get_optimized_diagonal_moves(sorted_fields, possible_moves):
    """
    Identifies the best diagonal moves based on the number of occupied fields.

    Args:
        sorted_fields (dict): A dictionary of diagonal indices and their respective counts.
        possible_moves (list): A list of available moves.

    Returns:
        dict: A sorted dictionary of moves and their corresponding priority.
    """
    # Prioritize diagonal moves with the most fields occupied by the player.
    best_moves = {}
    diagonal_moves = [[1, 5, 9], [3, 5, 7]]  # Diagonal move mappings.

    for diag_index, appearance_count in sorted_fields.items():
        for move in possible_moves:
            if move in diagonal_moves[diag_index]:
                best_moves[move] = appearance_count

    return sort_dictonary(best_moves)

def get_horizontal_counts(game_board, player_symbol):
    """
    Counts the number of fields occupied by the player in each row.

    Args:
        game_board (list): The current game board represented as a 2D list.
        player_symbol (str): The symbol of the player ('X' or 'O').

    Returns:
        dict: A sorted dictionary of row indices and their respective counts.
    """
    # Analyze each row to count how many positions are occupied by the player.
    count_each_row = {}
    prev_rows = 0
    for row_index in range(len(game_board)):
        num_of_appearances = 0
        for col_index in range(len(game_board[row_index])):
            if game_board[row_index][col_index] == player_symbol:
                move = row_index + prev_rows + col_index + 1
                num_of_appearances += 1
        count_each_row[row_index] = num_of_appearances
        prev_rows += 2
    return sort_dictonary(count_each_row)

def sort_dictonary(dictionary):
    """
    Sorts a dictionary by values in descending order.

    Args:
        dictionary (dict): The dictionary to be sorted.

    Returns:
        dict: A sorted dictionary.
    """
    # Return the dictionary sorted by its values (highest first).
    return dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))

def transposed(game_board):
    """
    Transposes the game board to convert rows into columns and vice versa.

    Args:
        game_board (list): The current game board represented as a 2D list.

    Returns:
        list: The transposed game board.
    """
    # Flip rows and columns in the game board.
    return [[game_board[j][i] for j in range(len(game_board))] for i in range(len(game_board[0]))]

def get_vertical_counts(game_board, player_symbol):
    """
    Counts the number of fields occupied by the player in each column.

    Args:
        game_board (list): The current game board represented as a 2D list.
        player_symbol (str): The symbol of the player ('X' or 'O').

    Returns:
        dict: A sorted dictionary of column indices and their respective counts.
    """
    # Count the number of positions in each column occupied by the player.
    return get_horizontal_counts(transposed(game_board), player_symbol)

def get_optimized_straight_moves(sorted_fields, possible_moves, horizontal=True):
    """
    Identifies the best moves based on rows or columns with the highest occupancy.

    Args:
        sorted_fields (dict): A dictionary of indices (rows or columns) and their respective counts.
        possible_moves (list): A list of available moves.
        horizontal (bool): Whether to optimize for rows (True) or columns (False).

    Returns:
        dict: A dictionary of moves and their priorities.
    """
    # Prioritize moves in rows or columns with the highest occupancy by the player.
    all_moves = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Row-wise mappings.
    if not horizontal:
        all_moves = transposed(all_moves)  # Column-wise mappings.

    best_moves = {}
    for row_index, appearance_count in sorted_fields.items():
        for move in possible_moves:
            if move in all_moves[row_index]:
                best_moves[move] = appearance_count

    return best_moves

def make_random_move(game_board):
    """
    Selects a random valid move from the available options.

    Args:
        game_board (list): The current game board represented as a 2D list.

    Returns:
        int: A random valid move.
    """
    # Randomly choose a move from the available options.
    possible_moves = get_possible_moves(game_board)
    while True:
        random_move = random.randint(1, 9)
        if random_move in possible_moves:
            return random_move

def calc_optimized_move(game_board, player_symbol):
    """
    Calculates the most optimized move for a player based on strategic analysis.

    Args:
        game_board (list): The current game board represented as a 2D list.
        player_symbol (str): The symbol of the player ('X' or 'O').

    Returns:
        dict: A dictionary of optimized moves and their priorities.
    """
    # Combine strategies for rows, columns, and diagonals to determine the optimal move.
    possible_moves = get_possible_moves(game_board)

    sorted_horizontal_fields = get_horizontal_counts(game_board, player_symbol)
    sorted_vertical_fields = get_vertical_counts(game_board, player_symbol)
    sorted_diagonal_fields = get_diagonal_counts(game_board, player_symbol)

    optimized_hori_moves = get_optimized_straight_moves(sorted_horizontal_fields, possible_moves, horizontal=True)
    optimized_verti_moves = get_optimized_straight_moves(sorted_vertical_fields, possible_moves, horizontal=False)
    optimized_diag_moves = get_optimized_diagonal_moves(sorted_diagonal_fields, possible_moves)

    optimized_diag_pref_moves = get_sorted_moves(optimized_diag_moves, optimized_verti_moves)
    optimized_final_moves = get_sorted_moves(optimized_diag_pref_moves, optimized_hori_moves)

    return optimized_final_moves

def make_smart_move(game_board, player_symbol, opponent_symbol):
    """
    Determines the best move for a player while minimizing the opponent's chances of winning.

    Args:
        game_board (list): The current game board represented as a 2D list.
        player_symbol (str): The symbol of the current player ('X' or 'O').
        opponent_symbol (str): The symbol of the opponent ('X' or 'O').

    Returns:
        int: The most strategic move available.
    """
    # Calculate moves to maximize the player's chances while blocking the opponent.
    curr_player_optimized_moves = calc_optimized_move(game_board, player_symbol)
    opponent_optimized_moves = calc_optimized_move(game_board, opponent_symbol)

    min_max_sorted_moves = get_sorted_moves(curr_player_optimized_moves, opponent_optimized_moves)
    final_moves = list(min_max_sorted_moves.keys())

    return final_moves[0] if final_moves else -1

def accuracy_rate(player_wins, total_rounds):
    """
    Calculates the winning percentage of a player.

    Args:
        player_wins (int): The number of games won by the player.
        total_rounds (int): The total number of games played.

    Returns:
        float: The winning percentage of the player.
    """
    # Calculate the percentage of games won by the player.
    return (player_wins / total_rounds) * 100

def get_sorted_moves(optimized_horizontal_moves, optimized_vertical_moves):
    """
    Combines and sorts moves based on priority from two dictionaries.

    Args:
        optimized_horizontal_moves (dict): Dictionary of horizontal moves and their priorities.
        optimized_vertical_moves (dict): Dictionary of vertical moves and their priorities.

    Returns:
        dict: A sorted dictionary of combined moves and their priorities.
    """
    # Merge the dictionaries and prioritize moves with the highest value.
    combined_moves = defaultdict(int)
    for moves in (optimized_horizontal_moves, optimized_vertical_moves):
        for key, value in moves.items():
            combined_moves[key] = max(combined_moves[key], value)
    return sort_dictonary(combined_moves)


"""
# Example, with which you can test the functions to find the optimal move

test_board = [
    ["O", "O", "X"],  # Row 1
    ["X", "", "X"],  # Row 2
    ["_", "O", "_"]   # Row 3
]

possible_moves = get_possible_moves(test_board)

sorted_horizontal_fields = get_horizontal_counts(test_board, "X")
sorted_vertical_fields = get_vertical_counts(test_board, "X")
sorted_diagonal_fields = get_diagonal_counts(test_board, "X")

optimized_hori_moves = get_optimized_straight_moves(sorted_horizontal_fields, possible_moves, horizontal = True)
optimized_verti_moves = get_optimized_straight_moves(sorted_vertical_fields, possible_moves, horizontal = False)
optimized_diag_moves = get_optimized_diagonal_moves(sorted_diagonal_fields, possible_moves)

print("optimized horizontal move: ", optimized_hori_moves)
print("optimized vertiical move: ", optimized_verti_moves)
print("optimized diagional move: ", optimized_diag_moves)

optimized_straight_moves = get_sorted_moves(optimized_diag_moves, optimized_verti_moves)
optimized_final_moves = get_sorted_moves(optimized_straight_moves, optimized_hori_moves)

print("opti: ", optimized_final_moves)
"""