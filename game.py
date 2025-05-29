#Author: Jasmeen Kaur
#Date: March 15, 2023
#Title : game.py
#Purpose : to run the game
from tkinter import *
import tkinter as tk
import tkinter.font as font
from fifteen import Fifteen

class Game:
    def __init__(self, master):
        self.gui = master
        self.gui.title("Fifteen Puzzle")
        self.font = font.Font(family="Helvetica", size=18, weight="bold")
        self.board = Fifteen()
        self.make_buttons()

    def click_button(self, value):
        if value == "shuffle":
            self.board.shuffle()
            self.make_buttons()
        elif self.board.is_valid_move(value):
            self.board.update(value)
            self.make_buttons()

    def make_buttons(self):
        button_props = {'bg': 'white', 'fg': 'black', 'font': self.font, 'height': 2, 'width': 5}
        for i in range(16):
            text = tk.StringVar()
            if self.board.tiles[i] == 0:
                text.set('')
            else:
                text.set(str(self.board.tiles[i]))
            name = str(self.board.tiles[i])
            button = tk.Button(self.gui, textvariable=text, name=name, command=lambda value=name: self.click_button(value), **button_props)
            if i == 0:
                button.grid(row=0, column=0)
            elif i % 4 == 0:
                button.grid(row=i//4, column=0)
            else:
                button.grid(row=i//4, column=i%4)
            if self.board.tiles[i] == 0:
                button.configure(bg='gray')
            else:
                button.configure(bg='white')
            self.gui.nametowidget(name).configure(bg='white')

        shuffle_button = tk.Button(self.gui, text="Shuffle", name="shuffle", command=lambda: self.click_button("shuffle"), **button_props)
        shuffle_button.grid(row=4, column=0)

    def run(self):
        self.gui.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    game = Game(root)
    game.run()