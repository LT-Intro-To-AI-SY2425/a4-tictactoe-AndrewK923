# Assignment 4 - Writeup

In assignment 4 we created a basic tic tac toe game so that we could learn object oriented programming. Respond to the following questions.

## Reflection Questions

1. What was the most difficult part to tic-tac-toe?
Getting the has_won to work properly and pass the asserts. 

2. Explain how you would add a computer player to the game.
You would add a user input statement before the if statement in the make_move method. 

3. If you add a computer player, explain (doesn't have to be super technical) how you might get the computer player to play the best move every time. *Note - I am not grading this for a correct answer, I just want to know your thoughts on how you might accomplish it.
I would check if the computer player is placing its X or O next to or adjacent to another one of its X's or O's. Maybe also checking if making the move will get you to the win condition (check win condition before making move). 