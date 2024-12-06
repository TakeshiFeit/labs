from tkinter import *
from tkinter import messagebox
import sys

class TicTacToe():
    def __init__(self, root, sign):
        self.root = root

        self.board = [None]*9

        if sign == True: self.Player_sign, self.Pc_sign = "X", "0"
        else: self.Player_sign, self.Pc_sign = "0", "X"

        self.buttons = []
        self.good_pos = [[0,1,2],[3,4,5],[6,7,8],
               [0,4,8],[2,4,6],
               [0,3,6],[1,4,7],[2,5,8]]
        row = []

        for i in range(3):
            for j in range(3):
                btn = Button(self.root, text = None, height = 16, width = 32, command = lambda i = i, j = j: self.click(i, j))
                btn.grid(row = i, column = j)
                row.append(btn)
        self.buttons.append(row)
        if self.Player_sign == "0":
            self.first_bot()

    def click(self, i, j):
        if self.board[i*3+j] == None:
            self.board[i*3+j] = self.Player_sign
            self.buttons[0][i*3+j].config(text = self.Player_sign)
            self.check_win()

            step = self.pc_step()
            self.board[step] = self.Pc_sign
            self.buttons[0][step].config(text = self.Pc_sign)
            self.check_win()

    def first_bot(self):
        step = self.pc_step()
        self.board[step] = self.Pc_sign
        self.buttons[0][step].config(text = self.Pc_sign)
        self.check_win()

    def minimax(self, board, depth, is_maximazing):
        if self.is_win(self.Pc_sign, board):
            return 100
        if self.is_win(self.Player_sign, board):
            return -100
        if all(board):
            return 0

        if is_maximazing:
            best_score = -sys.maxsize
            for i in range(9):
                if board[i] == None:
                    board[i] = self.Pc_sign
                    score = self.minimax(board, depth+1, False)
                    board[i] = None
                    best_score = max(best_score, score)
        else:
            best_score = sys.maxsize
            for i in range(9):
                if board[i] == None:
                    board[i] = self.Player_sign
                    score = self.minimax(board, depth+1, True)
                    board[i] = None
                    best_score = min(best_score, score)
        return best_score

    def pc_step(self):
        best_score = -sys.maxsize
        move = None
        board = [0] * 9
        for i in range(9):
            board[i] = self.board[i]
        for i in range(9):
            if board[i] == None:
                board[i] = self.Pc_sign
                score = self.minimax(board, 0, False)
                board[i] = None
                if score > best_score:
                    best_score = score
                    move = i
        return move

    def is_win(self, sign ,board):
        for a, b, c in self.good_pos:
            if board[a] == board[b] == board[c] == sign:
                return True
        return False

    def check_win(self):
        for a, b, c in self.good_pos:
            if self.board[a] == self.board[b] == self.board[c] and self.board[c] != None:
                messagebox.showinfo(title = "Result", message = f"{self.board[c]} win")
                sys.exit(0)
        if all(self.board):
            messagebox.showinfo(title = "Result", message = "Draw")
            sys.exit(0)

def choice():
    while True:
        if messagebox.askyesno(title="Question", message="Would you like to play for X ?"):
            return True
        if messagebox.askyesno(title="Question", message="Would you like to play for 0 ?"):
            return False

root = Tk()
root.resizable(0,0)
TicTacToe(root, choice())
root.mainloop()