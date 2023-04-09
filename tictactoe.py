import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic-Tac-Toe")
        self.turn = "X"
        self.buttons = []
        self.create_board()

    def create_board(self):
        for i in range(3):
            row = []  # Create an empty list to represent the current row
            for j in range(3):
                # Create a Tkinter button with text="", font=("Arial", 20), width=5, and height=2.
                # The button calls the method button_click() with the arguments (i, j) when clicked.
                button = tk.Button(self.master, text="", font=("Arial", 20), width=5, height=2,
                                command=lambda i=i, j=j: self.button_click(i, j))
                # Place the button in the i-th row and j-th column of the grid
                button.grid(row=i, column=j)
                # Add the button to the current row
                row.append(button)
            # Add the current row to the list of buttons
            self.buttons.append(row)

    def button_click(self, i, j):
        # Get a reference to the button that was clicked
        button = self.buttons[i][j]
        # Check if the button is already marked (i.e. its text is not "")
        if button["text"] == "":
            # If the button is not marked, mark it with the current player's symbol (X or O)
            button["text"] = self.turn
            # Check if the current player has won the game
            if self.check_win():
                # If the current player has won, show a message box with the winner's name
                messagebox.showinfo("Game Over", f"{self.turn} wins!")
                # Ask the user if they want to play again or quit the game
                if messagebox.askyesno("Play Again?", "Do you want to play again?"):
                    # If the user wants to play again, reset the board for a new game
                    self.reset_board()
                else:
                    # If the user wants to quit, destroy the game window to exit the program
                    self.master.destroy()
            # If there is no winner yet and the board is full, the game is a tie
            elif self.check_tie():
                # Show a message box indicating that the game is a tie
                messagebox.showinfo("Game Over", "Tie!")
                # Ask the user if they want to play again or quit the game
                if messagebox.askyesno("Play Again?", "Do you want to play again?"):
                    # If the user wants to play again, reset the board for a new game
                    self.reset_board()
                else:
                    # If the user wants to quit, destroy the game window to exit the program
                    self.master.destroy()
            else:
                # If the game is not over, switch to the other player's turn
                self.change_turn()

    def check_win(self):
        # Check rows
        for i in range(3):
            # Check if all the buttons in the i-th row have the same non-empty text
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
                return True
        # Check columns
        for j in range(3):
            # Check if all the buttons in the j-th column have the same non-empty text
            if self.buttons[0][j]["text"] == self.buttons[1][j]["text"] == self.buttons[2][j]["text"] != "":
                return True
        # Check diagonals
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            return True
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            return True
        # If no winning condition is found, return False
        return False

    def check_tie(self):
        for i in range(3):
            for j in range(3):
                # If any button is empty, the game is not a tie
                if self.buttons[i][j]["text"] == "":
                    return False
        # If all buttons are non-empty and no player has won, the game is a tie
        return True

    def change_turn(self):
        # This function switches the current player to the other player for each turn.
        # If the current player is "X", change the turn to "O", and vice versa.
        if self.turn == "X":  # Check if the current turn is for "X"
            self.turn = "O"  # If so, change the turn to "O"
        else:
            self.turn = "X"  # Otherwise, change the turn to "X"

    def reset_board(self):
        # This function resets the board by clearing the text of all buttons and setting the turn to "X".
        for i in range(3):  # Loop through the rows of the board
            for j in range(3):  # Loop through the columns of the board
                self.buttons[i][j]["text"] = ""  # Clear the text of the current button
        self.turn = "X"  # Set the turn to "X", since the first player is always "X"

if __name__ == "__main__":
    root = tk.Tk()
    ttt = TicTacToe(root)
    root.mainloop()
