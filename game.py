#Author: Jasmeen Kaur

#Purpose of this file: To run the game

from tkinter import *
import tkinter as tk
import tkinter.font as font
from fifteen import Fifteen
from tkinter import messagebox 


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
            return
        try:
            move = int(value)
        except ValueError:
            return
            
        if self.board.is_valid_move(value):
            self.board.update(value)
            self.make_buttons()

            if self.board.is_solved():
                messagebox.showinfo("You Win!", "Congratulations! You solved the puzzle!")

    def make_buttons(self):
        button_props = {'bg': 'white', 'fg': 'black', 'font': self.font, 'height': 2, 'width': 5}

        for i in range(16):
            text = tk.StringVar()
            tile_value = self.board.tiles[i]

            display = '' if tile_value == 0 or tile_value == '  ' else str(tile_value)
            text.set(display)

            button = tk.Button(self.gui, textvariable=text, command=lambda v=tile_value: self.click_button(v), **button_props)

            button.grid(row=i//4, column=i%4)

            if tile_value == 0 or tile_value == '  ':
                button.configure(bg='gray')
            else:
                button.configure(bg='white')

        shuffle_button = tk.Button(self.gui, text="Shuffle", name="shuffle", command=lambda: self.click_button("shuffle"), **button_props)
        shuffle_button.grid(row=4, column=0)

    def run(self):
        self.gui.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    game = Game(root)
    game.run()