import sys,os
import curses
import time
import locale
import pdb
locale.setlocale(locale.LC_ALL, '')

class BeatGrid :
    def __init__(self, grid_data, stdscr):
        self.grid_data = grid_data
        self.map = [['no_key']*grid_data['columns'] for ii in range(grid_data['rows'])]
        #self.draw_grid(grid_data)
        screen_height, screen_width = stdscr.getmaxyx()

   
    def draw_grid(self, stdscr):
        for ii in range (self.grid_data['columns']):
            for jj in range (self.grid_data['rows']):
                self.draw_cell(ii*(self.grid_data['cell_width']+1),jj*(self.grid_data['cell_height'] +1),stdscr)


      
    def draw_cell(self, xpos, ypos, stdscr):
        height = self.grid_data['cell_height']
        width = self.grid_data['cell_width']
      
        for ii in range(height) :
            for jj in range(width):
                stdscr.addch(ypos + ii, xpos+ jj, curses.ACS_CKBOARD)

   #column = beats, row = instrument

def draw_menu(stdscr):
    k=0
    
    while k!= ord('q'):
        x = 0

        grid_data = {'rows': 3, 'columns':8, 'cell_width':5, 'cell_height':3}
    
        bg = BeatGrid(grid_data, stdscr)
        bg.draw_grid(stdscr)
        # Clear and refresh the screen for a blank canvas
        k = stdscr.getch()



    
if __name__ == "__main__":
    curses.wrapper(draw_menu)

