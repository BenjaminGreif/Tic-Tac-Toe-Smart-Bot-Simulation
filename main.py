import board
import smart_bot

# Display a welcome message at the start of the game
board.welcome()

# Initialize two players: one "dumb" and one "smart" AI bot
player_1 = board.initialize_bot(0, "Patric Star", "X", "dumb")  # Dumb AI bot named Patric Star
player_2 = board.initialize_bot(1, "Spock", "O", "smart")       # Smart AI bot named Spock

# Set the limit for the number of rounds
round_limit = 1000
round = 0

# Loop to play multiple rounds of Tic-Tac-Toe
while round < round_limit:
    game_board = board.get_board()  # Reset the game board for each new round
    board.init_board(game_board)    # Initialize/reset the game board

    while True:
        # Player 1 (or current player) makes a move
        board.make_move(player_1, game_board, player_2)
        board.draw_board(game_board)  # Display the updated board

        # Check if Player 1 has won
        if board.check_win(game_board, player_1):
            board.print_winner(player_1)
            break

        # Check if the game ended in a draw
        if board.check_draw(game_board):
            board.print_draw()
            break

        # Switch players: Player 1 becomes Player 2 and vice versa
        player_1, player_2 = player_2, player_1

    # Increment the round counter after each game
    round += 1

# After all rounds, display the final results
board.print_final_stats(round)

# Determine the overall winner and loser based on the number of wins
winners = board.get_winners(player_1, player_2)
winner = winners[0]
loser = winners[1]

# Print the number of wins for the winner and loser
print(f"{winner['name']} wins: {winner['wins']}")
print(f"{loser['name']} wins: {loser['wins']}")

# Calculate and print the number of draws
# Total draws are equal to the total rounds minus the sum of the players' wins
draws = round - player_1['wins'] - player_2['wins']
print(f"Draws: {draws}")

# Calculate the accuracy rate of the AI (percentage of games won by the overall winner)
acc_rate = smart_bot.accuracy_rate(winner['wins'], round)
board.print_accuracy_rate(acc_rate)



