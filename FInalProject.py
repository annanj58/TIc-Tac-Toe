#Author: Joshua Annan
#Date: May 5th, 2024
#This programs that lets the user place tic tac toe. 

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        # Images for main menu and buttons
        tic_tac_toe_img = Image.open("tictactoe.png")
        play_button = Image.open("play-button.png")
        logout_button = Image.open("logout.png")

        play_button = play_button.resize((50, 50))
        logout_button = logout_button.resize((50, 50))

        self.photo = ImageTk.PhotoImage(tic_tac_toe_img)
        self.playbutton = ImageTk.PhotoImage(play_button)
        self.logoutbutton = ImageTk.PhotoImage(logout_button)

        # Packing components on startup
        self.text_widget = tk.Label(root, text="Welcome to Tic Tac Toe")
        self.text_widget.pack()

        self.image_label = tk.Label(root, image=self.photo)
        self.image_label.pack()

        self.start_button = tk.Button(root, image=self.playbutton , command=self.start_game)
        self.start_button.pack(pady=10)

        self.exit_button = tk.Button(root, image=self.logoutbutton, command=self.exit_game)
        self.exit_button.pack(pady=10)

    def start_game(self):
        self.start_button.destroy()
        self.exit_button.destroy()

        self.game_window = tk.Toplevel(self.root)
        self.game_window.title("Tic Tac Toe Game")

        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]

        # Create buttons for game board
        self.buttons = []
        for i in range(3):
            row_buttons = []
            for j in range(3):
                button = tk.Button(self.game_window, text="", width=10, height=4, command=lambda i=i, j=j: self.make_move(i, j))
                button.grid(row=i, column=j)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def make_move(self, row, col):
        if self.board[row][col] == "":
            self.buttons[row][col].config(text=self.current_player)
            self.board[row][col] = self.current_player
            if self.check_winner(row, col):
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_game()
            else:
                self.switch_player()

    def check_winner(self, row, col):
        # Check row
        if self.board[row][0] == self.board[row][1] == self.board[row][2] == self.current_player:
            return True
        # Check column
        if self.board[0][col] == self.board[1][col] == self.board[2][col] == self.current_player:
            return True
        # Check diagonal
        if (row == col and
            self.board[0][0] == self.board[1][1] == self.board[2][2] == self.current_player) or \
           (row + col == 2 and
            self.board[0][2] == self.board[1][1] == self.board[2][0] == self.current_player):
            return True
        return False

    def check_draw(self):
        for row in self.board:
            if "" in row:
                return False
        return True

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")
                self.board[i][j] = ""
        self.current_player = "X"

    def exit_game(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()





