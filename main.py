import sys,os
import curses
import mido
import time
import locale
import pdb
locale.setlocale(locale.LC_ALL, '')

output = mido.open_output('IAC Driver Bus 1')
msg = mido.Message('note_on')

def draw_menu(stdscr):
    k = 0
    cursor_x = 0
    cursor_y = 0
    x = 0;

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    while (k != ord('q')):
        # Loop where k is the last character pressed
         if (x<7):
            x += 1
         elif(x==7):
            x=0


         # Initialization
         stdscr.clear()
         height, width = stdscr.getmaxyx()

         count = {1: curses.ACS_CKBOARD, 2: '-', 3: '-', 4: '-', 5: '-', 6: '-', 7: '-', 8: '-'}
         count_list = ['-', '-', '-', '-', '-', '-', '-', '-']

            
         count_list[x] = curses.ACS_CKBOARD


         if k == curses.KEY_DOWN:
             cursor_y = cursor_y + 1
         elif k == curses.KEY_UP:
             cursor_y = cursor_y - 1
         elif k == curses.KEY_RIGHT:
             cursor_x = cursor_x + 1
         elif k == curses.KEY_LEFT:
             cursor_x = cursor_x - 1

         cursor_x = max(0, cursor_x)
         cursor_x = min(width-1, cursor_x)

         cursor_y = max(0, cursor_y)
         cursor_y = min(height-1, cursor_y)

         # Declaration of strings
         title = "Curses example"[:width-1]
         subtitle = "{}  {}  {}  {}  {}  {}  {}  {}".format(count[1],count[2],count[3],count[4],count[5],count[6],count[7],count[8])[:width-1]
         
         keystr = "Last key pressed: {}".format(k)[:width-1]
         statusbarstr = "Press 'q' to exit | STATUS BAR | Pos: {}, {}".format(cursor_x, cursor_y)
         if k == 0:
             keystr = "No key press detected..."[:width-1]

         #play sound
         msg.note = cursor_x/2 +50
         msg.velocity = cursor_y + 64
         output.send(msg)

            # Centering calculations
         start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
         start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
         start_x_keystr = int((width // 2) - (len(keystr) // 2) - len(keystr) % 2)
         start_y = int((height // 2) - 2)

         # Rendering some text
         whstr = "Width: {}, Height: {}".format(width, height)
         stdscr.addstr(0, 0, whstr, curses.color_pair(1))

         # Render status bar
         stdscr.attron(curses.color_pair(3))
         stdscr.addstr(height-1, 0, statusbarstr)
         stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
         stdscr.attroff(curses.color_pair(3))

         # Turning on attributes for title
         stdscr.attron(curses.color_pair(2))
         stdscr.attron(curses.A_BOLD)

            # Rendering title
         stdscr.addstr(start_y, start_x_title, title)

         # Turning off attributes for title
         stdscr.attroff(curses.color_pair(2))
         stdscr.attroff(curses.A_BOLD)

         # Print rest of text
         for ii,ch in enumerate(count_list):
            stdscr.addch(start_y + 1, start_x_subtitle+ii, ch)

         stdscr.addstr(start_y + 3, (width // 2) - 2, '-' * 4)
         stdscr.addstr(start_y + 5, start_x_keystr, keystr)
         stdscr.move(cursor_y, cursor_x)

            # Refresh the screen
         stdscr.refresh()

         curses.halfdelay(3)
         k = stdscr.getch()

            


def main():
    curses.wrapper(draw_menu)

if __name__ == "__main__":
    main()