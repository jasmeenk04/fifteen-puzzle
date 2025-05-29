#Author: Jasmeen Kaur
#Date: March 15, 2023
#Title : fifteen.py

import numpy as np
from random import choice

class Fifteen:
    
    def __init__(self, size = 4):
        self.tiles = [i for i in range(1, size ** 2)] + ['  ']
        
        # adjacency matrix for sliding puzzle game
        #inner lists contains the indices of the neighboring tiles 
        self.adj = [        [1, 4],
            [0, 2, 5],
            [1, 3, 6],
            [2, 7],
            [0, 5, 8],
            [1, 4, 6, 9],
            [2, 5, 7, 10],
            [3, 6, 8, 11],
            [4, 7, 9, 12],
            [5, 8, 10, 13],
            [6, 9, 11, 14],
            [7, 10, 15],
            [8, 13],
            [9, 12, 14],
            [10, 13, 15],
            [11, 14]
        ]

    def update(self, move):
        #is move is valid??
        if self.is_valid_move(move):
            #indices of the selected tile
            tile_index = self.tiles.index(move)
            empty_index = self.tiles.index('  ')
            
            # swap
            Fifteen.transpose(self, tile_index, empty_index)
        
    def transpose(self, i, j):
        # SWAPPP
        self.tiles[i], self.tiles[j] = self.tiles[j], self.tiles[i]
    
        #returns the statussss
        return self.tiles
    

    def shuffle(self, steps=30):
        #index of space
        empty_index = self.tiles.index('  ')
        
        for zebra in range(steps):
            move_index = choice(self.adj[empty_index])
            #swap again
            self.tiles[empty_index], self.tiles[move_index] = self.tiles[move_index], self.tiles[empty_index]
            
            #updated index
            empty_index = move_index
        
        
    def is_valid_move(self, move):
        blank_index = self.tiles.index('  ')
        move_index = self.tiles.index(move)
        
        # is it moved??
        for adjacent_index in self.adj[blank_index]:
            if move_index == adjacent_index:
                return True
        
        # move is invalid is its not straight
        return False
    

    def is_solved(self):
        target_tiles = [i for i in range(1, 16)] + ['  ']

        if self.tiles == target_tiles:
            return True
        else:
            return False

    def draw(self):
        row_sep = '+---' * 4 + '+\n'
        col_sep = '|'
        #template
        row_template = col_sep + ' {:2} ' + col_sep + ' {:2} ' + col_sep + ' {:2} ' + col_sep + ' {:2} ' + col_sep + '\n'
        
        print(row_sep + row_template.format(*self.tiles[0:4]) + row_sep
            + row_template.format(*self.tiles[4:8]) + row_sep
            + row_template.format(*self.tiles[8:12]) + row_sep
            + row_template.format(*self.tiles[12:16]) + row_sep)
        
    def __str__(self): #long ass code for titles
        return f'{self.tiles[0]:2} {self.tiles[1]:2} {self.tiles[2]:2} {self.tiles[3]:2} \n{self.tiles[4]:2} {self.tiles[5]:2} {self.tiles[6]:2} {self.tiles[7]:2} \n{self.tiles[8]:2} {self.tiles[9]:2} {self.tiles[10]:2} {self.tiles[11]:2} \n{self.tiles[12]} {self.tiles[13]} {self.tiles[14]} {self.tiles[15]} \n'


            
if __name__ == '__main__':
    
    game = Fifteen()
    assert (str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n')
    assert game.is_valid_move(15) == True
    assert game.is_valid_move(12) == True
    assert game.is_valid_move(14) == False
    assert game.is_valid_move(1) == False
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14    15 \n'
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == True
    game.shuffle()
    assert str(game) != ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == False
    
    
    '''You should be able to play the game if you uncomment the code below'''

    game = Fifteen()
    game.shuffle()
    game.draw()
    while True:
        move = input('Enter your move or q to quit: ')
        if move == 'q':
            break
        elif not move.isdigit():
            continue
        game.update(int(move))
        game.draw()
        if game.is_solved():
            break
    print('Game over!')

    
    
        
