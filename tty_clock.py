import curses
import time
import os
import sys
import cursor
import argparse
parser = argparse.ArgumentParser(description="displays a simple stopwatch")
parser.set_defaults(mode=curses.A_BOLD)
parser.add_argument("--highlight", help="highlights the time", action="store_const", dest="mode", const=curses.A_STANDOUT)
parser.add_argument("--show_cursor", help="doesn't hide the terminal cursor", action="store_true")
args = parser.parse_args()
if not args.show_cursor:
    cursor.hide()
def terminal_size():
    x = os.get_terminal_size().columns
    y = os.get_terminal_size().lines
    return [x, y]
def get_time():
    current_time = time.localtime()
    hour = str(current_time.tm_hour)
    minute = str(current_time.tm_min)
    second = str(current_time.tm_sec)
    return f"{hour}:{minute}:{second}"
screen = curses.initscr()
time_displaying = True
while time_displaying:
    try:
       screen.clear()
       current_time = get_time()
       console_size = terminal_size()
       x, y = console_size[0] // 2 - 4, console_size[1] // 2
       screen.addstr(y,x,current_time,args.mode)
       screen.refresh()
    except KeyboardInterrupt:
        curses.endwin()
        time_displaying = False
sys.exit(0)
