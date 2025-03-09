# Tic-Tac-Toe: Smart Bot Simulation

A smart Tic-Tac-Toe bot designed to maximize its winning chances by strategically selecting the best game moves. In this simulation, a smart bot plays against a dumb bot that makes random moves. Unlike classical machine learning approaches, the smart bot uses a **unique rule-based logic system** I developed to systematically identify and rank game moves in descending order of winning potential. The project demonstrates **algorithmic problem solving**, **systematic strategy design**, and **simulation design**. In extensive simulations, the smart bot consistently achieves a **95-97% win rate** over 1,000 games, reflecting a thoughtful, data-driven approach to developing and validating strategic algorithmic solutions.

---

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Algorithm Overview](#algorithm-overview)
4. [Quick Start](#quick-start)
5. [Project Structure](#project-structure)
6. [Next Steps & Future Plans](#next-steps--future-plans)
7. [Contact](#contact)

---

## Overview

This project simulates a series of Tic-Tac-Toe matches between two bots:
- **Smart Bot**: Employs a custom rule-based logic system to choose the best move.
- **Dumb Bot**: Selects moves at random, serving as a baseline opponent.

The simulation demonstrates that even with a simple game, a thoughtfully designed algorithm can produce outstanding results.

---

## Features

- **Algorithmic Problem Solving**: The smart bot systematically evaluates game moves to maximize winning chances.
- **Systematic Strategy Design**: Uses a unique rule-based logic system rather than traditional machine learning methods.
- **Simulation Design**: Extensive testing over 1,000 games shows a consistent **95-97% win rate**.

---

## Algorithm Overview

The algorithm ranks potential moves by counting how many stones a player already occupies in each vertical, horizontal, and diagonal line. Moves with the highest occupied counts in their respective line are prioritized. When counts are equal, diagonal moves are favored because they require using the center square — a critical point that also contributes to horizontal and vertical wins. By focusing on the diagonal, we leverage a win condition that overlaps with other winning lines, thereby enhancing our overall winning chances. 

### Algorithm for `calc_optimized_move`

1. Start with `get_possible_moves` for a player.
2. Count the number of stones the player already occupies along the horizontal, vertical and diagonal lines for each move (`get_horizontal_counts`, `get_vertical_counts`, `get_diagonal_counts`).
3. Sort the possible moves based on the stone count in their respective straight (horizontal & vertical) and diagonal lines (`get_optimized_straight_moves`, `get_optimized_diagonal_moves`).
4. Merge and sort diagonal and vertical moves first, prioritizing diagonal moves to `get_sorted_moves`.
5. For each move during `get_sorted_moves`, record only the highest stone count among the horizontal, vertical, and diagonal counts, then return a list sorted in ascending order .

### Algorithm for `make_smart_move`

1. Use `calc_optimized_move` for the current player to maximize winning chances.
2. Use `calc_optimized_move` for the opponent to minimize the opponent's winning chances.
3. Use `get_sorted_moves` to merge and sort the moves that maximize the current player's chances and minimize the opponent's chances.
4. Return the first move from the ascending-sorted list of all possible moves.

---

## Quick Start

To run the simulation:

1. **Clone or Download** this repository.
2. **Run the Simulation**:
   ```
   python main.py
   ```
   The console will display game updates and the final results.

*(No external dependencies are required.)*

---

## Project Structure

```
.
├── README.md         # Project documentation
├── main.py           # Main script to run the game loop
├── board.py          # Handles board representation and state checking
├── smart_bot.py      # Contains the smart bot's rule-based logic and algorithm
└── random_bot.py     # Implements the dumb bot's random move logic
```

---

## Next Steps & Future Plans

- **Enhance the AI**:  
  Explore integrating more advanced strategies such as alpha-beta pruning or reinforcement learning methods.
  
- **Data Logging & Visualization**:  
  Log game data for further analysis and visualization to better understand performance trends.
  
- **User Interaction**:  
  Develop a graphical user interface or web interface to allow users to play against the smart bot.
  
- **Expand Simulations**:  
  Test the smart bot against multiple variants or other AI strategies to benchmark performance further.

---

## Contact

- **Name**: Benjamin Greif
- **LinkedIn**: www.linkedin.com/in/benjamin-greif

Feel free to reach out with any questions, suggestions, or collaboration ideas!
