import sys
import pygame
import numpy as np
from constants import *

#Pygame SETUP
pygame.init()
screen = pygame.display.set_mode(( width,height ))
pygame.display.set_caption('TIC TAC TOE ML')
screen.fill(bg_color)

class Board:

    def __init__(self):
        self.squares = np.zeros( (rows,cols))
       

    def mark_sqr(self,row,col,player):
        self.squares[row][col] = player

    def empty_sqr(self,row,col):
        return self.squares[row][col] == 0

class Game:
    def __init__(self):

        self.board = Board()
        self.player = 1
        self.show_lines()
    
    def show_lines(self):
        #vertical
        pygame.draw.line(screen,line_color,(square_size,0) ,(square_size,height) ,line_width)
        pygame.draw.line(screen,line_color,(width - square_size,0) ,(width - square_size,height) ,line_width)
        
        #horizontal
        pygame.draw.line(screen,line_color,(0,square_size) ,(width,square_size) ,line_width)
        pygame.draw.line(screen,line_color,(0,height - square_size) ,(width, height-square_size) ,line_width)

    def draw_fig(self,row,col):
        if self.player ==1:
            #draw corss
            #1st line
            start_dir = (col*square_size + offset,row * square_size + offset)
            end_dir = (col*square_size+square_size - offset,row * square_size+square_size - offset)
            pygame.draw.line(screen,cross_color,start_dir,end_dir,cross_width)
           
            #2nd line           
            start_dir = (col*square_size + offset,row * square_size+square_size - offset)
            end_dir = (col*square_size+square_size - offset,row * square_size + offset)
            pygame.draw.line(screen,cross_color,start_dir,end_dir,cross_width)
        elif self.player ==2:
            #draw circle
            center = (col * square_size + square_size //2,row  * square_size + square_size //2)
            pygame.draw.circle(screen,circ_color,center,radius,circ_width)

    def next_turn(self):
        self.player = self.player%2 + 1
def main():
    #obj
    game = Game()
    board = game.board

    #main loop
    while True:

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // square_size
                col = pos[0] // square_size
                
                if board.empty_sqr(row,col):
                    game.board.mark_sqr(row , col, game.player)
                    game.next_turn()
                    game.draw_fig(row, col)

                    print(board.squares)

        pygame.display.update()
main()