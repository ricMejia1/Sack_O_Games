# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name(s):         Saylor Sherrodd
#                   Ricardo Mejia
# Section:         574
# Assignment:   Game 2
# Date:         7 1 2022
#

from random import randint
from keyboard import is_pressed
import time

begin = '\x1b[1m' 
end = '\x1b[39m\x1b[22m' 
colors = {'red' : '\x1b[31m', 'green' : '\x1b[32m'} 


chars = { #colored squares for the board in a dict for easy reference
    'apple' : begin + colors['red'] + chr(9632) + end,
    'snake' : begin + colors['green'] + chr(9632) + end,
    'empty' : chr(9633)
}

size = 9 #this will affect the board size

def randSpace():
    """
    

    Returns
    -------
    tuple
        tuple of 2 random ints less than the size.

    """
    return randint(0, size-1),randint(0,size-1) #useful function for random space

def display(table, num1): 
    """
    

    Parameters
    ----------
    table : iterable
        iterable of iterables of characters.
    num1 : int
        number to be printed below table.

    Returns
    -------
    None.

    """

    print('\n'*10)
    for i in table: print(' '.join(i))
    print(f'Your score is {num1}')

def appleTest(a,b): 
    """
    

    Parameters
    ----------
    a : int
        Xpos.
    b : int
        Ypos.

    Returns
    -------
    None.

    """
    global applex, appley
    if round(a) == applex and round(b) == appley:
        newApple(False)
        
def newApple(already): 
    """
    

    Parameters
    ----------
    already : bool
        whether or not we have already generated a new apple.

    Returns
    -------
    None.

    """
    global applex, appley, score, eaten, tail
    if not already:
        tail.append( (applex,appley) )
        score += 1
    applex,appley = randSpace()
    if (applex,appley) in tail: newApple(True)
    eaten = True

def giveTutorial():
    input('To play snake, use WASD to move the head of the snake around. Hitting a wall will put you out the other side. Move the head of your snake into an apple to eat it and get longer. If you run into the body of the snake, you die. Push Q to quit. Enjoy!')
    

def playSnake(tutorial = False):
    """
    

    Returns
    -------
    None.

    """
    global eaten, applex, appley, tail, score    
    if tutorial: giveTutorial()
    board = [[chars['empty'] for i in range(size)] for i in range(size)] #creates the board

    
    x,y = randSpace()
    tail = []
    board[y][x] = chars['snake'] #set up random snake start

    applex,appley = randSpace() #set up random apple start

    speed =.60
    x = 0
    y = 0
    dy = 0
    dx = 0
    score = 0
    
    while score <= size**2:
        time.sleep(.001)
        if is_pressed('q'): break #quit
        board = [[chars['empty'] for i in range(size)] for i in range(size)] #clear bard
        board[round(y)][round(x)] = chars['snake'] #draw snake head
        
        for i in tail: board[i[1]][i[0]] = chars['snake'] #draw snake tail
        currentPos = (round(x),round(y)) #get current position so we can compare and see if we've moved the head
        board[appley][applex] = chars['apple'] #draw apple
        
        display(board,score) 
        
        if is_pressed('w') and dy == 0: #go up
            dy = -.09*speed
            dx = 0
            x = round(x)
        if is_pressed('s') and dy == 0: #go down
            dy = .09*speed
            dx = 0
            x = round(x)
        if is_pressed('a') and dx == 0: #go left
            dx = -.09*speed
            dy = 0
            y = round(y)
        if is_pressed('d') and dx == 0: #go right
            dx = .09*speed
            dy = 0
            y = round(y)
        
    
        y += dy #move the head
        x += dx  
        
        if currentPos != (round(x),round(y)) and len(tail) > 0: #if we've moved the head, move the tail and check for collision
            tail.pop(-1)
            tail.insert(0, currentPos)
            
            if sum([i.count(chars['snake']) for i in board]) != len(tail) + 1 and not eaten: #test for collision if the snake hasn't eaten an apple for a bit
                print('You died')
                if input('Would you like to play again? (y/n) : ').lower() == 'y': playSnake()
                break
            
            eaten = False
            
        appleTest(x,y)
            
        if not(0 <= x <= size-1): #wrap around for left/right
            if round(x) < 0: x += size
            if round(x) > size-1: x -= size
            
        if not(0 <= y <= size-1): #wrap around for up/down
            
            if round(y) < 0: y += size
            if round(y) > size-1: y -= size
    
    
    else: #win condition
        print('Uhhhhhhhhh... You win I guess. Good job')
