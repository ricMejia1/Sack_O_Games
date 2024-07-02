from tkinter import *
from tkinter import messagebox

pressed = True
index = 0

def startGame():
    """
    

    Returns
    -------
    None.

    """
    
    board = Tk()
    board.title("Tik Tac Toe Game")
    
    #board.geometry('250x250')
    
    #end
    #list
    #try except
    #loop
    
    pressed = True
    index = 0
    def helpInstructions():
        """
        

        Returns
        -------
        None.

        """
    	
        newWindow = Toplevel(board)
    
        newWindow.title("Instructions/Help")
    
        newWindow.geometry("400x200")
    
        Label(newWindow, 
           text ="\n\nthis is a multiplayer game. start X choose a box in the 3x3 grid.\n Click it and then it is O turn do this until the grid\n is full and you can not do anything else and have to restart or until\n the game declares a winner the restart button restarts\n the whole game and exit leaves the game.").pack()
    helpInstructions()
    def reset():
        """
        

        Returns
        -------
        None.

        """
        global pressed, index
        pressed = True
        index = 0
        
    
        
        def disable_btns():
            """
            

            Returns
            -------
            None.

            """
            while True:
                disabled = list(btn1.config(state=DISABLED), btn2.config(state=DISABLED), btn3.config(state=DISABLED),
                btn4.config(state=DISABLED), btn5.config(state=DISABLED), btn6.config(state=DISABLED), btn7.config(state=DISABLED),
                btn8.config(state=DISABLED), btn9.config(state=DISABLED))
                
    
    
        def winnerTTT():
            """
            

            Returns
            -------
            None.

            """
            global winner
            
            winner = False
    
            
            if btn1['text'] == 'x' and btn2['text'] == 'x' and btn3['text'] == 'x':
                btn1.config(bg='yellow')
                btn2.config(bg='yellow')
                btn3.config(bg='yellow')
                winner = True
                messagebox.showinfo("Tic Tac Toe", "Player X wins!")
                disable_btns()
            elif btn4['text'] == 'x' and btn5['text'] == 'x' and btn6['text'] == 'x':
                btn4.config(bg ='yellow')
                btn5.config(bg='yellow')
                btn6.config(bg='yellow')
                winner = True
                messagebox.showinfo("Tic Tac Toe", "Player X wins!")
                disable_btns()
            elif btn7['text'] == 'x' and btn8['text'] == 'x' and btn9['text'] == 'x':
                btn7.config(bg='yellow')
                btn8.config(bg='yellow')
                btn9.config(bg='yellow')
                winner = True
                messagebox.showinfo("Tic Tac Toe", "Player X wins!")
                disable_btns()
            elif btn1['text'] == 'x' and btn4['text'] == 'x' and btn7['text'] == 'x':
                btn1.config(bg='yellow')
                btn4.config(bg='yellow')
                btn7.config(bg='yellow')
                winner = True
                messagebox.showinfo("Tic Tac Toe", "Player X wins!")
                disable_btns()
            elif btn2['text'] == 'x' and btn5['text'] == 'x' and btn8['text'] == 'x':
                btn2.config(bg='yellow')
                btn5.config(bg='yellow')
                btn8.config(bg='yellow')
                winner = True
                messagebox.showinfo("Tic Tac Toe", "Player X wins!")
                disable_btns()
            elif btn3['text'] == 'x' and btn6['text'] == 'x' and btn9['text'] == 'x':
                btn3.config(bg='yellow')
                btn6.config(bg='yellow')
                btn9.config(bg='yellow')
                winner = True
                messagebox.showinfo("Tic Tac Toe", "Player X wins!")
                disable_btns()
            elif btn1['text'] == 'x' and btn5['text'] == 'x' and btn9['text'] == 'x':
                btn1.config(bg='yellow')
                btn5.config(bg='yellow')
                btn9.config(bg='yellow')
                winner = True
                messagebox.showinfo("Tic Tac Toe", "Player X wins!")
                disable_btns()
            elif btn3['text'] == 'x' and btn5['text'] == 'x' and btn7['text'] == 'x':
                btn3.config(bg='yellow')
                btn5.config(bg='yellow')
                btn7.config(bg='yellow')
                winner = True
                messagebox.showinfo("Tic Tac Toe", "Player X wins!")
                disable_btns()
                
            elif btn1['text'] == 'o' and btn2['text'] == 'o' and btn3['text'] == 'o':
                btn1.config(bg='yellow')
                btn2.config(bg='yellow')
                btn3.config(bg='yellow')
                winner = True
                messagebox.showinfo("Tic Tac Toe", "Player O wins!")
                disable_btns()
            elif btn4['text'] == 'o' and btn5['text'] == 'o' and btn6['text'] == 'o':
                btn4.config(bg='yellow')
                btn5.config(bg='yellow')
                btn6.config(bg='yellow')
                winner = True
                messagebox.showinfo("Tic Tac Toe", "Player O wins!")
                disable_btns()
            elif btn7['text'] == 'o' and btn8['text'] == 'o' and btn9['text'] == 'o':
                btn7.config(bg='yellow')
                btn8.config(bg='yellow')
                btn9.config(bg='yellow')
                winner = True
                messagebox.showinfo("Tic Tac Toe", "Player O wins!")
                disable_btns()
            elif btn1['text'] == 'o' and btn4['text'] == 'o' and btn7['text'] == 'o':
                btn1.config(bg='yellow')
                btn4.config(bg='yellow')
                btn7.config(bg='yellow')
                winner = True
                messagebox.showinfo("Tic Tac Toe", "Player O wins!")
                disable_btns()
            elif btn2['text'] == 'o' and btn5['text'] == 'o' and btn8['text'] == 'o':
                btn2.config(bg='yellow')
                btn5.config(bg='yellow')
                btn8.config(bg='yellow')
                winner = True
                messagebox.showinfo("Tic Tac Toe", "Player O wins!")
                disable_btns()
            elif btn3['text'] == 'o' and btn6['text'] == 'o' and btn9['text'] == 'o':
                btn3.config(bg='yellow')
                btn6.config(bg='yellow')
                btn9.config(bg='yellow')
                winner = True
                messagebox.showinfo("Tic Tac Toe", "Player O wins!")
                disable_btns()
            elif btn1['text'] == 'o' and btn5['text'] == 'o' and btn9['text'] == 'o':
                btn1.config(bg='yellow')
                btn5.config(bg='yellow')
                btn9.config(bg='yellow')
                winner = True
                messagebox.showinfo("Tic Tac Toe", "Player O wins!")
                disable_btns()
            elif btn3['text'] == 'o' and btn5['text'] == 'o' and btn7['text'] == 'o':
                btn3.config(bg='yellow')
                btn5.config(bg='yellow')
                btn7.config(bg='yellow')
                winner = True
                messagebox.showinfo("Tic Tac Toe", "Player O wins!")
                disable_btns()
    
    
        def btn_clk(btn):
            """
            

            Parameters
            ----------
            btn : tkinter button object
                button changes the text from empty string to x or o depending on the Boolean value.

            Returns
            -------
            None.

            """
            global pressed, index
            
            if btn['text'] == ' ' and pressed == True:
                btn["text"] = 'x'
                pressed = False
                index += 1
                winnerTTT()
                
            elif btn['text'] == ' ' and pressed == False:
                btn['text'] = 'o'
                pressed = True
                index += 1
                winnerTTT()
                
            else:
                messagebox.showerror("Tic Tac Toe", "unavailable box, try again")
    
    
        btn1 = Button(board, text = " " , height = 6, width = 8, bg="red", command = lambda: btn_clk(btn1))
        btn2 = Button(board, text = " " , height = 6, width = 8, bg="red", command = lambda: btn_clk(btn2))
        btn3 = Button(board, text = " " , height = 6, width = 8, bg="red", command = lambda: btn_clk(btn3))
        btn4 = Button(board, text = " " , height = 6, width = 8, bg="red", command = lambda: btn_clk(btn4))
        btn5 = Button(board, text = " " , height = 6, width = 8, bg="red", command = lambda: btn_clk(btn5))
        btn6 = Button(board, text = " " , height = 6, width = 8, bg="red", command = lambda: btn_clk(btn6))
        btn7 = Button(board, text = " " , height = 6, width = 8, bg="red", command = lambda: btn_clk(btn7))
        btn8 = Button(board, text = " " , height = 6, width = 8, bg="red", command = lambda: btn_clk(btn8))
        btn9 = Button(board, text = " ", height = 6, width = 8, bg="red", command = lambda: btn_clk(btn9))
    
        buttonclose = Button(board, text="End Game", command=board.destroy).grid(row=4, column=2)
        helpBtn = Button(board, text="Help", command= lambda: helpInstructions()).grid(row=4, column=1)
        restartButton = Button(board, text="Restart", command=lambda: reset()).grid(row=4, column=0)
        btn1.grid(row=0, column=0)
        btn2.grid(row=0, column=1)
        btn3.grid(row=0, column=2)
        btn4.grid(row=1, column=0)
        btn5.grid(row=1, column=1)
        btn6.grid(row=1, column=2)
        btn7.grid(row=2, column=0)
        btn8.grid(row=2, column=1)
        btn9.grid(row=2, column=2)
    
    
    
    def disable_btns():
        """
        

        Returns
        -------
        None.

        """
        btn1.config(state=DISABLED)
        btn2.config(state=DISABLED)
        btn3.config(state=DISABLED)
        btn4.config(state=DISABLED)
        btn5.config(state=DISABLED)
        btn6.config(state=DISABLED)
        btn7.config(state=DISABLED)
        btn8.config(state=DISABLED)
        btn9.config(state=DISABLED)
    
    
    
    
    
    def winnerTTT():
        """
        

        Returns
        -------
        None.

        """
        global winner
        
        winner = False
    
        
        if btn1['text'] == 'x' and btn2['text'] == 'x' and btn3['text'] == 'x':
            btn1.config(bg='yellow')
            btn2.config(bg='yellow')
            btn3.config(bg='yellow')
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Player X wins!")
            disable_btns()
        elif btn4['text'] == 'x' and btn5['text'] == 'x' and btn6['text'] == 'x':
            btn4.config(bg ='yellow')
            btn5.config(bg='yellow')
            btn6.config(bg='yellow')
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Player X wins!")
            disable_btns()
        elif btn7['text'] == 'x' and btn8['text'] == 'x' and btn9['text'] == 'x':
            btn7.config(bg='yellow')
            btn8.config(bg='yellow')
            btn9.config(bg='yellow')
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Player X wins!")
            disable_btns()
        elif btn1['text'] == 'x' and btn4['text'] == 'x' and btn7['text'] == 'x':
            btn1.config(bg='yellow')
            btn4.config(bg='yellow')
            btn7.config(bg='yellow')
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Player X wins!")
            disable_btns()
        elif btn2['text'] == 'x' and btn5['text'] == 'x' and btn8['text'] == 'x':
            btn2.config(bg='yellow')
            btn5.config(bg='yellow')
            btn8.config(bg='yellow')
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Player X wins!")
            disable_btns()
        elif btn3['text'] == 'x' and btn6['text'] == 'x' and btn9['text'] == 'x':
            btn3.config(bg='yellow')
            btn6.config(bg='yellow')
            btn9.config(bg='yellow')
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Player X wins!")
            disable_btns()
        elif btn1['text'] == 'x' and btn5['text'] == 'x' and btn9['text'] == 'x':
            btn1.config(bg='yellow')
            btn5.config(bg='yellow')
            btn9.config(bg='yellow')
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Player X wins!")
            disable_btns()
        elif btn3['text'] == 'x' and btn5['text'] == 'x' and btn7['text'] == 'x':
            btn3.config(bg='yellow')
            btn5.config(bg='yellow')
            btn7.config(bg='yellow')
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Player X wins!")
            disable_btns()
            
        elif btn1['text'] == 'o' and btn2['text'] == 'o' and btn3['text'] == 'o':
            btn1.config(bg='yellow')
            btn2.config(bg='yellow')
            btn3.config(bg='yellow')
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Player O wins!")
            disable_btns()
        elif btn4['text'] == 'o' and btn5['text'] == 'o' and btn6['text'] == 'o':
            btn4.config(bg='yellow')
            btn5.config(bg='yellow')
            btn6.config(bg='yellow')
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Player O wins!")
            disable_btns()
        elif btn7['text'] == 'o' and btn8['text'] == 'o' and btn9['text'] == 'o':
            btn7.config(bg='yellow')
            btn8.config(bg='yellow')
            btn9.config(bg='yellow')
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Player O wins!")
            disable_btns()
        elif btn1['text'] == 'o' and btn4['text'] == 'o' and btn7['text'] == 'o':
            btn1.config(bg='yellow')
            btn4.config(bg='yellow')
            btn7.config(bg='yellow')
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Player O wins!")
            disable_btns()
        elif btn2['text'] == 'o' and btn5['text'] == 'o' and btn8['text'] == 'o':
            btn2.config(bg='yellow')
            btn5.config(bg='yellow')
            btn8.config(bg='yellow')
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Player O wins!")
            disable_btns()
        elif btn3['text'] == 'o' and btn6['text'] == 'o' and btn9['text'] == 'o':
            btn3.config(bg='yellow')
            btn6.config(bg='yellow')
            btn9.config(bg='yellow')
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Player O wins!")
            disable_btns()
        elif btn1['text'] == 'o' and btn5['text'] == 'o' and btn9['text'] == 'o':
            btn1.config(bg='yellow')
            btn5.config(bg='yellow')
            btn9.config(bg='yellow')
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Player O wins!")
            disable_btns()
        elif btn3['text'] == 'o' and btn5['text'] == 'o' and btn7['text'] == 'o':
            btn3.config(bg='yellow')
            btn5.config(bg='yellow')
            btn7.config(bg='yellow')
            winner = True
            messagebox.showinfo("Tic Tac Toe", "Player O wins!")
            disable_btns()
    
    
    
    
    
    def btn_clk(btn):
        """
        

        Parameters
        ----------
        btn : tkinter button object
            button changes the text from empty string to x or o depending on the Boolean value.

        Returns
        -------
        None.

        """
        global pressed, index
        try:
            if btn['text'] == ' ' and pressed == True:
                btn["text"] = 'x'
                pressed = False
                index += 1
                winnerTTT()
                
            elif btn['text'] == ' ' and pressed == False:
                btn['text'] = 'o'
                pressed = True
                index += 1
                winnerTTT()
                
            else:
                messagebox.showerror("Tic Tac Toe", "unavailable box, try again")
        except:
            print("error")
    
    
    
    
    
    
    
    #btnList = list[board, text = " " , height = 5, width = 8, bg="yellow", command = lambda: btn_clk(btn1)]
    btn1 = Button(board, text = " " , height = 6, width = 8, bg="red", command = lambda: btn_clk(btn1))
    btn2 = Button(board, text = " " , height = 6, width = 8, bg="red", command = lambda: btn_clk(btn2))
    btn3 = Button(board, text = " " , height = 6, width = 8, bg="red", command = lambda: btn_clk(btn3))
    btn4 = Button(board, text = " " , height = 6, width = 8, bg="red", command = lambda: btn_clk(btn4))
    btn5 = Button(board, text = " " , height = 6, width = 8, bg="red", command = lambda: btn_clk(btn5))
    btn6 = Button(board, text = " " , height = 6, width = 8, bg="red", command = lambda: btn_clk(btn6))
    btn7 = Button(board, text = " " , height = 6, width = 8, bg="red", command = lambda: btn_clk(btn7))
    btn8 = Button(board, text = " " , height = 6, width = 8, bg="red", command = lambda: btn_clk(btn8))
    btn9 = Button(board, text = " ", height = 6, width = 8, bg="red", command = lambda: btn_clk(btn9))
    
    buttonclose = Button(board, text="End Game", command=board.destroy).grid(row=4, column=2)
    helpBtn = Button(board, text="Help", command= lambda: helpInstructions()).grid(row=4, column=1)
    restartButton = Button(board, text="Restart", command=lambda: reset()).grid(row=4, column=0)
    btn1.grid(row=0, column=0)
    btn2.grid(row=0, column=1)
    btn3.grid(row=0, column=2)
    btn4.grid(row=1, column=0)
    btn5.grid(row=1, column=1)
    btn6.grid(row=1, column=2)
    btn7.grid(row=2, column=0)
    btn8.grid(row=2, column=1)
    btn9.grid(row=2, column=2)
    
    board.mainloop()
    
