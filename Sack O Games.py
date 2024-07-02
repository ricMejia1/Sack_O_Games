# from tkinter import *
# import time
from mathGame import mathOverlord
from SnakeGame import playSnake
from tictactoe import startGame



# menu = Tk()
# menu.title("Main Menu")
# menu.geometry("200x200")


# text = Label(text="Sack O\' Games\n Menu")
# text.place(x=60,y=10)

# snake = Button(menu, text="Snake Game", command=lambda: playSnake()).place(x=65, y=50)
# TicTacToe = Button(menu, text="TicTacToe", command= lambda: startGame()).place(x=70, y=80)
# Math_Practice = Button(menu, text="Math Practice", command= lambda: mathOverlord()).place(x=60, y=110)

# quitBtn = Button(menu, text="Quit",bg="red", command=menu.destroy).place(x=85, y=170)


# class clock(Frame):
#     def __init__(self,master=None):
#         Frame.__init__(self, master)
#         self.master = master
#         self.label = Label(text="", fg="Green")
#         self.label.place(x=150,y=170)
#         self.timer()

#     def timer(self):
#         now = time.strftime("%H:%M:%S")
#         self.label.configure(text=now)
#         self.after(1000, self.timer)
# clock=clock(menu)
# menu.after(1000, clock.timer)
# menu.mainloop()
# menu.mainloop()

def tryInt(n):
    """
    

    Parameters
    ----------
    n : any
        thing to be attempted to turned into int. Typically an input().

    Returns
    -------
    int
        int of n.

    """
    try:
        if n == 'q': return 'q'
        return int(n)
    except ValueError:
        print('That\'s not a valid input, please try again.')
        return tryInt(input())

while True:
    
    cue = input('Type the corresponding number to play that game. Enter Q in this menu to exit the Sack O\' Games. Enjoy! \n\n1. Snake\n2. TicTacToe\n3. Math Practice\n\n').lower()
        
    cue = tryInt(cue)
    
    if cue == 'q': break

    
    if cue == 1: playSnake(True)
    elif cue == 2: startGame()
    elif cue == 3: mathOverlord()




    
