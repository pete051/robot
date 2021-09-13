import cursers
import RPi.GPIO as IO

screen=cursers.initscr()
cursers.noecho()
cursers.cbreak()
screen.keypad(True)

try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            break
        elif char == cursers.KET_UP:
            print("Up")
        elif char == cursers.KEY_DOWN:
            print("down")
        elif char == cursers.KEY_RIGHT:
            print("right")
        elif char == cursers.KEY_LEFT:
            print "left"
        elif char == 10:
            print "stop"
r
finally:
    cursers.nocheck(); screen.keypad(0); cursers.echo()
    cursers.endwin()
