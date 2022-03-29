# Paper, Scissors, Rock
You probably know the game ["Paper, Scissors, Rock"](https://en.wikipedia.org/wiki/Rock_paper_scissors). A game for two players. Each player has three options, namely paper, scissors, rock which are formed by the player's hand. The rules are quite easy: rock beats scissors, scissors beats paper, paper beats rock. If both players have chosen the same object, it's a draw.

In the following, we play 100 consecutive games. Each player has to hand in a file consisting of one letter per line. The letters are either "R", "S" or "P". 

Write a Python Program that reads two files `player1.txt` and `player2.txt`. These files are organized according to the above rules. The program should compare both inputs and calculate how many games have been won by player1, by player2 and how many games ended in a draw. The results are written into a file `result.txt` which looks as follows:

	Player1 wins: 23
	Player2 wins: 48
	Draws: 29
	
The sum should always be 100.

# Tests
- check if a file exist and contains the correct result
- check if two files are opened
- check if one file is written
- check if there is either a for or while loop containing an if-statement