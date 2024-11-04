import random
import numpy as np
import os

class Game2048:

    def __init__(self):
        self.grid = None     
        self.state = 'not over'   
    
    
    def initialize_grid(self):
        '''initialize the grid with two number 2'''
        try:

            self.grid = np.zeros((4, 4), dtype=int)

            self.add_new_number()
            self.add_new_number()

            self.display_instructions()
            self.display_grid()
        except Exception as e:
            print("An error occured while initializing the grid:")
            print(e)
    
    def display_instructions(self):
        print("Commands are as follows : ")
        print("'W' or 'w' : Move Up")
        print("'S' or 's' : Move Down")
        print("'A' or 'a' : Move Left")
        print("'D' or 'd' : Move Right")
        print("'Q' or 'q' : Quit Game")

    def display_grid(self):
        '''Display the current grid state in the terminal'''
        try:
            # print("\nCurrent Grid:")
            # for row in self.grid:
            #     print("\t".join(str(num) if num != 0 else '.' for num in row))
            # print()
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear console for a dynamic experience
            print("\n" + "=" * 25)
            print(" " * 7 + "2048 Game")
            print("=" * 25 + "\n")
            
            print("-" * 25)
            for row in self.grid:
                print("|", end="")
                for num in row:
                    if num == 0:
                        print("     |", end="")  # Empty cell
                    else:
                        print(f"{num:^5}|", end="")  # Center-aligned cell
                print("\n" + "-" * 25)
        except Exception as e:
            print("An error occured while displaying the grid:")
            print(e)

        
    def add_new_number(self):
        ''' randomly add a number 2 in an empty cell in the grid'''
        try:
            empty_cells = [(i, j) for i in range(4) for j in range(4) if self.grid[i][j] == 0]
            if not empty_cells:
                print("The grid is filled but you still have chance. Please enter w, a, s, d to move the tiles.")
                return
            row, col = random.choice(empty_cells)
            self.grid[row][col] = 2
        except Exception as e:
            print("An error occured while adding a new number:")
            print(e)


    def current_state(self):
        '''return the current state of the grid'''
        try:
            # if there is a 2048 tile in the grid, the player wins
            for row in self.grid:
                if 16 in row:
                    self.state = 'win'
                    return
            
            # if there are is empty cell, or if no empty cells but adjacent values can be merged, continue the game
            for i in range(3):
                for j in range(3):
                    if self.grid[i][j] == 0:
                        self.state = 'not over'
                        return
                    if self.grid[i][j] == self.grid[i+1][j] or self.grid[i][j] == self.grid[i][j+1]:
                        self.state = 'not over'
                        return
            
            for j in range(3):
                if self.grid[3][j] == 0 or self.grid[3][j+1] == 0 or self.grid[3][j] == self.grid[3][j+1]:
                    self.state = 'not over'
                    return
                
            for i in range(3):
                if self.grid[i][3] == 0 or self.grid[i+1][3] == 0 or self.grid[i][3] == self.grid[i+1][3]:
                    self.state = 'not over'
                    return
                
            self.state = 'lose'
            return
        except Exception as e:
            print("An error occured while checking the current state:")
            print(e)

    # 3. Move the tiles in the grid by pressing w, s, a, d for up, down, left, right respectively
    def move(self, direction):
        '''move the tiles in the grid'''
        try:
            if direction == 'w':
                self.move_up()
            elif direction == 's':
                self.move_down()
            elif direction == 'a':
                self.move_left()
            elif direction == 'd':
                self.move_right()

            else:
                print("Invalid input! Use 'w', 's', 'a', 'd' to move.")
                return

            self.add_new_number()
            self.display_grid()
        except Exception as e:
            print("An error occured while moving the tiles:")
            print(e)
            
    
    def slide_and_merge_rows(self, row):
        '''slide and merge the tiles in a row to the left'''
        try:
            # slide the tiles
            row = [i for i in row if i != 0]
            row += [0] * (4 - len(row))

            # merge the tiles
            for i in range(3):
                if row[i] == row[i+1]:
                    row[i] *= 2
                    row[i+1] = 0

            # slide row again after merging
            row = [i for i in row if i != 0]
            row += [0] * (4 - len(row))
            return row
        except Exception as e:
            print("An error occured while sliding and merging the rows:")
            print(e)
    

    def move_left(self):
        '''move the tiles up'''
        try:
            for row in range(4):
                self.grid[row] = self.slide_and_merge_rows(self.grid[row])
        except Exception as e:
            print("An error occured while moving the tiles left:")
            print(e)
    
    def move_right(self):
        '''move the tiles down'''
        try:
            for row in range(4):
                self.grid[row] = self.slide_and_merge_rows(self.grid[row][::-1])[::-1]
        except Exception as e:
            print("An error occured while moving the tiles right:")
            print(e)    

    def move_up(self):
        '''move the tiles left'''
        try:
            self.grid = self.grid.T
            self.move_left()
            self.grid = self.grid.T
        except Exception as e:
            print("An error occured while moving the tiles up:")
            print(e)
    
    
    def move_down(self):
        '''move the tiles right'''
        try:
            self.grid = self.grid.T
            self.move_right()
            self.grid = self.grid.T
        except Exception as e:
            print("An error occured while moving the tiles down:")
            print(e)
            
    
    def play(self):
        '''play the game'''
        try:
            # start the
            self.initialize_grid()
            while self.state == 'not over':
                direction = input("Enter your move: ")
                if direction == 'q' or direction == 'Q':
                    print('Game quit.')
                    return
                self.move(direction)
                self.current_state()
            
            if self.state == 'win':
                print("Congratulations! You have reached 2048.")
            else:
                print("Game Over!")
            
            self.restart()
        except Exception as e:
            print("An error occured while playing the game:")
            print(e)

    def restart(self):
        '''Ask the player if they want to restart the game'''
        while True:
            try:
                choice = input("Do you want to restart the game? (y/n): ").lower().strip()
                if choice == 'y':
                    self.grid = None     
                    self.state = 'not over'
                    self.play()
                    break
                elif choice == 'n':
                    print("Thanks for playing!")
                    break
            except Exception as e:
                print(f"Error processing restart choice: {e}")


