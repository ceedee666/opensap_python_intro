You probably know the game ["Rock, Paper, Scissors"](https://en.wikipedia.org/wiki/Rock_paper_scissors). A game for two
players. Each player has three options, namely rock, paper, scissors, which are formed by the player's hand. The rules
are quite easy:
- rock beats scissors
- scissors beats paper
- paper beats rock.

If both players have chosen the same object, it's a draw.

In the following, we play 100 consecutive games. Each player has to hand in a file consisting of one letter per line.
The letters are either "R", "P" or "S".

Write a Python program that reads two files `player1.txt` and `player2.txt`. These files are organized according to the
above rules. The program should compare both inputs and calculate how many games have been won by player1, by player2
and how many games ended in a draw. The results are written into a file `result.txt` which looks as follows:

	Player1 wins: 23
	Player2 wins: 48
	Draws: 29

<br/>

The sum should always be 100.


**Please note:**
When programming your solution in CodeOcean, files created by your program will not be visible. If you want to check the
content of those files, we suggest to let your code run on your machine (e.g. in a Jupyter Notebook) and check the
content of the files there.