import smart_bot

# Initialize the Tic-Tac-Toe board with empty fields
# Each row is represented as a list
# "_" indicates an empty field

tic_tac_toe_board = [
    ["_", "_", "_"],  # Row 1
    ["_", "_", "_"],  # Row 2
    ["_", "_", "_"]   # Row 3
]

# Function to return a copy of the current board
# Used to avoid direct modification of the original board
def get_board():
    return [row[:] for row in tic_tac_toe_board]

# Function to visually display the board
# Each row is printed with fields separated by '|'
def draw_board(board):
    for row in board:
        print(" | ".join(row))
    print()  # Adds a blank line for better readability

# Utility function to print a separator line
# Helps in formatting the output for better clarity
def print_section(s_length=57, symbol="="):
    print(symbol * s_length)

# Function to display a welcome message
def welcome():
    print_section()
    print("Let's play Tic-Tac-Toe! :-)")
    print_section()

# Function to initialize a bot with given attributes
# Attributes include name, symbol (e.g., 'X' or 'O'), and IQ level ('dumb' or 'smart')
def initialize_bot(player_number, name_KI, symbol, IQ):
    print(f"The AI bot {name_KI} is being initialized.")
    print_section()
    return {'name': name_KI, 'number': player_number, 'wins': 0, 'symbol': symbol, 'IQ': IQ}

# Function to display the current win status of both players
def draw_player_status(player_1, player_2):
    for player in [player_1, player_2]:
        print(f"Player {player['name']} wins: {player['wins']}")
    print_section()

# Function to explain the move numbering system
# Demonstrates how the board is numbered from 1 to 9
def explain_move():
    print("The board is numbered from 1 to 9:")
    draw_board(tic_tac_toe_board)

# Function to reset the game board to its initial state
def init_board(game_board):
    for row in range(3):
        for col in range(3):
            game_board[row][col] = "_"

# Function to make a move for the current player
# Handles input validation, ensures moves are valid, and updates the board
def make_move(curr_player, game_board, opponent):
    while True:
        print(f"AI {curr_player['name']} is making its move!")

        # Decision based on IQ level ('dumb' or 'smart')
        if curr_player['IQ'] == "dumb":
            move = str(smart_bot.make_random_move(game_board))  # Random move
        elif curr_player['IQ'] == "smart":
            move = str(smart_bot.make_smart_move(game_board, curr_player['symbol'], opponent['symbol']))  # Optimized move

        # Validate that move is numeric
        if not move.isdigit():
            print("Error: Please enter a valid number.")
            continue

        move = int(move)

        # Check if move is within valid range (1-9)
        if move < 1 or move > 9:
            print("Error: The number must be between 1 and 9.")
            continue

        # Map move to row and column indices on the board
        row = (move - 1) // 3
        col = (move - 1) % 3

        # Ensure the chosen field is empty
        if game_board[row][col] != "_":
            print("Error: The field is already occupied.")
            continue

        # Update the board with the player's symbol
        game_board[row][col] = curr_player['symbol']
        return

# Function to announce the winner and increment their win count
def print_winner(player):
    print_section()
    print(f"{player['name']} has won!")
    print_section()
    player['wins'] += 1

# Function to check if a player has won the game
# Looks for 3 matching symbols in a row, column, or diagonal
def check_win(game_board, player):
    for i in range(3):
        # Check rows
        if all(game_board[i][j] == player['symbol'] for j in range(3)):
            return True
        # Check columns
        if all(game_board[j][i] == player['symbol'] for j in range(3)):
            return True

    # Check diagonals
    if all(game_board[i][i] == player['symbol'] for i in range(3)):
        return True
    if all(game_board[i][2 - i] == player['symbol'] for i in range(3)):
        return True

    return False

# Function to check if the game is a draw
# Returns True if all fields are occupied without a winner
def check_draw(game_board):
    return all(cell != "_" for row in game_board for cell in row)

# Function to display the final statistics after all rounds
def print_final_stats(round):
    print_section(symbol="*")
    print(f"Final score after {round} rounds!")
    print_section(symbol="*")
    print_section()
    print(f"Total games played: {round}")

# Function to print the accuracy rate of the AI
def print_accuracy_rate(acc_rate):
    print_section()
    print(f"Accuracy Rate: {acc_rate:.2f} %")
    print_section()

# Function to sort players by wins in descending order
# Used to determine overall winners
def get_winners(player_1, player_2):
    players = [player_1, player_2]
    sorted_players = sorted(players, key=lambda player: player['wins'], reverse=True)
    return sorted_players

# Function to announce a draw in case of no winner
def print_draw():
    print_section()
    print("Draw. No winner.")
    print_section()





