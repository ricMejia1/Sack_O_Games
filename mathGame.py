from time import perf_counter
from random import randint
from math import ceil


def tryIntInput(message):
    """
    

    Parameters
    ----------
    message : String
        Message to be displayed to user.

    Returns
    -------
    int
        Response from user.

    """
    
    try:
        entered = input(message).lower()
        if entered == 'q': return 'break'
        return int(entered)
    
    except ValueError:
        return tryIntInput('That didn\'t work, please try that again. \n' + message)

def genNdigit(n):
    """
    

    Parameters
    ----------
    n : int
        Number of digits.

    Returns
    -------
    tuple of integers
        X,Y cordinates for a random space.

    """
    num = ''
    for i in range(n):
        num += str(randint(0,9))
    if num[0] == '0': num = genNdigit(n)
    
    return int(num)

def display(numbers , operation):
    """
    

    Parameters
    ----------
    numbers : tuple
        A tuple of numbers which the function will display.
    operation : str
        The symbol used in the math problem (EX. +, -, x, /).

    Returns
    -------
    None.

    """
    print(f' {numbers[0]}\n{operation}{numbers[1]}\n',end = '')
    print('-'*(len(str(numbers[0]))+1) )

def playMultiplication(digits, n = 1, score = 0):    
    """
    

    Parameters
    ----------
    digits : int
        Number of digits in the problems..
    n : int, optional
        number of iterations completed. The default is 1.
    score : int, optional
        number of correct answers. The default is 0.

    Returns
    -------
    None.

    """
    
    global s, t0
    if n == 1: t0 = perf_counter()
    if digits == 'break': return None

    print()
    if n > 10: 
        s = score
        return 'done'
    
    num1 = genNdigit(digits)
    num2 = genNdigit(digits)
    
    answer = num1 * num2

    nums = (num1, num2)
    
    display(nums, 'x')
    
    if input() == str(answer): playMultiplication(digits, n+1, score + 1)    
    else: playMultiplication(digits, n+1, score)
    

def playDivision(digits, n = 1, score = 0):
    """
    

    Parameters
    ----------
    digits : int
        Number of digits in the problems..
    n : int, optional
        number of iterations completed. The default is 1.
    score : int, optional
        number of correct answers. The default is 0.

    Returns
    -------
    None.

    """
    
    global s, t0
    if n == 1: t0 = perf_counter()
    if digits == 'break': return None

    print()
    if n > 10: 
        s = score
        return 'done'
    
    num1 = genNdigit(digits)
    num2 = genNdigit(digits)
    
    if num1 < num2: 
        nums = (num1,num2)
        num2, num1 = nums[0], nums[1]
        
    num1 = ceil(num1 / num2)*num2
    
    answer = int(num1/num2)
    
    nums = (num1, num2)
    
    display(nums, '/')
    
    if input() == str(answer): playDivision(digits, n+1, score + 1)    
    else: playDivision(digits, n+1, score)

def playSubtraction(digits, n = 1, score = 0):
    """
    

    Parameters
    ----------
    digits : int
        Number of digits in the problems..
    n : int, optional
        number of iterations completed. The default is 1.
    score : int, optional
        number of correct answers. The default is 0.

    Returns
    -------
    None.

    """
        
    global s, t0
    if n == 1: t0 = perf_counter()
    if digits == 'break': return None

    print()
    if n > 10: 
        s = score
        return 'done'
    
    num1 = genNdigit(digits)
    num2 = genNdigit(digits)
    
    answer = num1 - num2
    
    if answer < 0: 
        nums = (num1,num2)
        num2, num1 = nums[0], nums[1]
        answer *= -1
    
    nums = (num1, num2)

    display(nums, '-')
    
    if input() == str(answer): playSubtraction(digits, n+1, score + 1)    
    else: playSubtraction(digits, n+1, score)    
    
def playAddition(digits, n = 1, score = 0):
    """
    

    Parameters
    ----------
    digits : int
        Number of digits in the problems.
    n : int, optional
        number of iterations completed. The default is 1.
    score : int, optional
        number of correct answers. The default is 0.

    Returns
    -------
    None.

    """
    
    global s, t0
    if n == 1: t0 = perf_counter()
    if digits == 'break': return None

    print()
    if n > 10: 
        s = score
        return 'done'
    
    num1 = genNdigit(digits)
    num2 = genNdigit(digits)
    
    answer = num1 + num2

    nums = (num1, num2)

    display(nums, '+')
    
    if input() == str(answer): playAddition(digits, n+1, score + 1)    
    else: playAddition(digits, n+1, score)    

def chooseGame(cue):
    """
    

    Parameters
    ----------
    cue : int
        which math game to play.

    Returns
    -------
    float
        Time taken to solve math problems.

    """
    
    if cue == 1:
        playMultiplication(tryIntInput('How many digits would you like? '))#
    elif cue == 2:
        playDivision(tryIntInput('How many digits would you like? '))#
    elif cue == 3:
        playSubtraction(tryIntInput('How many digits would you like? '))#
    elif cue == 4:
        playAddition(tryIntInput('How many digits would you like? '))#
    else: 
        return None
    
    t1 = perf_counter()
    return t1 - t0
        
        
def mathOverlord():
    """
    

    Returns
    -------
    None.

    """
    global s
    s = 0
    print('Let\'s do some math practice. Sorry to whoever has to grade this, but you\'ll need to do some math practice. Good Luck!')
    print('\nTo select your operation, type the corresponding number. Afterward, input the number of digits, and then to answer each question, type the answer and push enter. Enter Q to quit. You will have to do 10 questions, and they are timed. You will be told your score at the end. To skip a problem, just push enter.')
    print('\nPS: Using a calculator is cheating. I know that\'s like the whole point of computer science, but like cmon. That\'s no fun. Yes you can use scratch paper.')
    print('Also, there are no bare except clauses here, so CTRL + C will work if you want to quit')
    print()
    time = chooseGame(tryIntInput('1. Multiplication \n2. Division \n3. Subtraction \n4. Addition \n'))
    if time == None: return None
    print()
    print(f'You got {s}/10 questions right in {time:.2f} seconds')
    if input('Would you like to play again? (y/n) ') == 'y': mathOverlord()
    
