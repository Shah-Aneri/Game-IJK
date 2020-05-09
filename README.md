# Game-IJK


We have used Minimax Algorithm with alpha-beta pruning to decide the best move to be played by our program while
playing against a human. The approach uses the snake shaped heuristic to decide the maximum utility value and based on 
that generating the best possible move for either max or min player. We have implemented our Minimax algorithm with
iterative deepening search having the depth of 5.

State Space:- 6*6 game board configuration.

Initial State:- 6*6 board configuration with A placed at a predictable empty position on the board if it Deterministic mode 
and A placed at any random position if it is Non-Deterministic mode.

Goal State:- The state when k or K appears on the board or the board is full.

Evaluation Function(Heuristic):- We have used snake shaped heuristic to find the best possible move that can be made by
max or min player in order to win the game.


Done by: Aneri Shah, Dhruva Bhavsar, Hely Modi
