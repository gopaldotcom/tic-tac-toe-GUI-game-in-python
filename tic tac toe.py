import tkinter as tk
import tkinter.messagebox as mb

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")

        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.current_player = "X"
        self.button = [[None for _ in range(3)] for _ in range(3)]
        self.player1_score = 0
        self.player2_score = 0

        self.create_buttons()
        self.create_score_label()

    def create_buttons(self):
        for row in range(3):
            for col in range(3):
                self.button[row][col] = tk.Button(self.root, text="", width=15, height=8,
                                                  command=lambda r=row, c=col: self.button_click(r, c))
                self.button[row][col].grid(row=row, column=col)

    def create_score_label(self):
        self.score_label = tk.Label(self.root, text=f"Player X: {self.player1_score} - Player O: {self.player2_score}")
        self.score_label.grid(row=3, column=0, columnspan=3)

    def check_win(self):
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != "":
                return self.board[row][0]

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != "":
                return self.board[0][col]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return self.board[0][2]

        return None

    def check_tie(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == "":
                    return False
        return True

    def button_click(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.button[row][col].config(text=self.current_player)

            winner = self.check_win()
            if winner:
                if winner == "X":
                    self.player1_score += 1
                else:
                    self.player2_score += 1
                mb.showinfo("Game Over", f"Player {winner} wins!")
                self.disable_buttons()
                self.reset_game()
            elif self.check_tie():
                mb.showinfo("Game Over", "It's a tie!")
                self.disable_buttons()
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def disable_buttons(self):
        for row in range(3):
            for col in range(3):
                self.button[row][col].config(state=tk.DISABLED)

    def reset_game(self):
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.current_player = "X"
        for row in range(3):
            for col in range(3):
                self.button[row][col].config(text="", state=tk.NORMAL)
        self.score_label.config(text=f"Player X: {self.player1_score} - Player O: {self.player2_score}")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
