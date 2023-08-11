# Tic-Tac-Toe Predictor 

## Goal
Design a Tic-Tac-Toe solver capable of predicting the outcome of a specific game when a board is provided, assuming both players are playing optimally. 

## Program 
The program takes as input an array of size 9 (indices 0-8 representing the blocks) and a number representing which player plays next (1 for "X" and 2 for "O"). 

<img width="295" alt="image" src="https://github.com/VihaanShah26/TicTacToe_Predictor/assets/79374408/5a3fef26-e083-4578-a5b1-e5e0fc64d6b1">

The array contains 0 for empty squares on the board, 1 for "X" and 2 for "O".

<img width="136" alt="image" src="https://github.com/VihaanShah26/TicTacToe_Predictor/assets/79374408/6a5ef716-19d9-427f-9de6-0b5cb731cf79">

The above board will be represented as: board = [1,2,0,0,1,0,0,0,0] 

The concept of min-max is being used to simulate two agents playing optimally against each other to explore the entire solution space. Then, alpha-beta pruning has been used to trim the solution space, thus making the program more efficient. 
