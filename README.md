# mazeMaker
Python code to generate and play maze in the terminal. Refreshes by clearing the terminal and printing the next frame. Generator may flicker a lot for larger maze sizes or some terminals.


# The maze generator - gen.py
Uses DFS to generate a square maze of user specified dimensions (5 to 50, but <25 recommended if you want to watch it generate). 
You have options to watch the algorithm work and save the resulting maze to a txt file. 
The start is markes with 's' end is 'e' and walls are either '_' or '|'.

Run: 'python gen.py'

Use: Follow prompts, pretty straightforward.

# Play - play.gen
Select a locally stored maze from a list. Play using WASD or Arrow Keys to move the player ('o').
Once you reach the end ('e') the game will end with the message "You Win!"

# Both - main.py
This just runs both files, generate then play.

Run: 'python main.py'
