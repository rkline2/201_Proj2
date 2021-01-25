# Sim
## 1. Description
For this project, you will be coding the game Sim. The "board" is a regular hexagon of points,
numbered 1 to 6. Players take turns drawing lines between the points in their own color.
The player that draws a line completing a triangle terminating in the numbered points LOSES.

## 2. The Setup
The game begins with no lines drawn. You will ask each player to pick a single character
to represent the "color" of their line. You will need to validate that they picked two different single characters.

## 3. Taking a Move
Before the player’s turn prompt them for a move. They will give the move astwo integers with a space in between.
If the integers are NOT valid moves, you will reprompt them.
* Players may not draw lines over already drawn lines<br>
* Players may not draw lines from one point to itself<br>
* The order of the numbers does NOT matter. For instance, 1 2 is thesame line as 2 1<br>

## 4. Turn Flow
A turn is comprised of the following:<br>
  1.The board is displayed.<br>
  2.The user is prompted for a move<br>
  3.The user inputs the move<br>
  4.The turn control swaps to the other player. Steps 1-4 are repeated until the game ends.<br>

## 5. End of the Game
The game ends when one player completes a triangle with corners at the numbered points.
At that time, the board is printed one last time, and the loser is declared
