'''Date:Mar. 3, 2019
   Author:Andrew Lin
   Description: A Connect Four game in Python where a
   human player plays against the computer.
'''

def add_to_hall_of_fame():
    '''A function that is called whenever the user wins the game it asks for their 
    name and appends it to a text file called “HallOfFame.txt”.'''
    file=open("HallOfFame.txt","a")
    new_winner=input("Please Enter Your Name: ")
    file.write(new_winner+"\n")
    print("Name has been added to the Hall of Fame")
    file.close()
        
def display_hall_of_fame():
    ''' This function displays the names stored in the Hall Of Fame, numbers 
    each name starting with 1. If the “HallOfFame.txt” file does not exist or is empty, then 
    the message “No Human Has Ever Beat Me..mwah-ha-ha-ha!” should be displayed instead.'''
    file=open("HallOfFame.txt","r")    
    content=file.read()
    if content=="":
        print("No Human Has Ever Beat Me..mwah-ha-ha-ha!")
        file.close()
        
    elif content!="":
        content=content.split("\n")
        print("Hall Of Fame:")
        for count in range(0,len(content)-1):
            print(str(count+1)+"."+content[count])
        file.close()

def get_winner(board,row,col):
    '''A function that takes in the board,row and columns values to determine whether 
    there is a winner,loser or stalemate.  The function will return the value in the board
    to check which is the winner.'''
    
    #Horizontal wins. Uses row and col values in a for loop to check for elements within a list that are the same.  
    for row_check in range(row):
        for col_check in range(col-3):
            if board[row_check][col_check] != " " and board[row_check][col_check]== board[row_check][col_check+1] == board[row_check][col_check+2] == board[row_check][col_check+3]:
                return board[row_check][col_check]
            
    #Vertical wins. Uses row and col values in a for loop to check for elements within a list that are the same.  
    for row_check in range(row-3):
        for col_check in range(col):
            if board[row_check][col_check] != " " and board[row_check][col_check]== board[row_check+1][col_check] == board[row_check+2][col_check] == board[row_check+3][col_check]:
                return board[row_check][col_check]
        
    #Checks for wins that are diagonals that are upward sloping (/). Uses row and col values in a for loop to check for elements within a list that are the same diagonally.  
    for row_check in range(row-3):
        for col_check in range(col-3):
            if board[row_check][col_check] != " " and board[row_check][col_check]== board[row_check+1][col_check+1] == board[row_check+2][col_check+2] == board[row_check+3][col_check+3]:
                return board[row_check][col_check]  
            
    #Diagonals that are downward sloping (\). Uses row and col values in a for loop to check for elements within a list that are the same diagonally.  
    for row_check in range(3,row):
        for col_check in range(col-3):
            if board[row_check][col_check] != " " and board[row_check][col_check]== board[row_check-1][col_check+1] == board[row_check-2][col_check+2] == board[row_check-3][col_check+3]:
                return board[row_check][col_check]      
    
    #A stalemate instance
    return""

def create_board(row,col): 
    '''This function takes two variables, row and col, and creates the board in a form of a nested list, 
    out of those values.  The function then returns the board as a list and the row
    and col values.'''
    
    board=[]
    for createRow in range(row):
        for createCol in range(col+1):
            string=" a"*createCol  #'a' is used to split the string into a List easier
            string=string[:len(string)-1]
            string=string.split("a")
        board.append(string)
    return board,row,col
    
def display_board(board,row,col):
    '''This function takes the parameter variables of the board,row,and column values and 
    displays the playing board of connect 4.'''
    
    dotted_line=col
    for name in range(col):
        print(str(name)+"   ",end="")
    print("")
    for row in board:
        for col in row:
            print(col+" | ",end="")
        print("")
        print("----"*(dotted_line))

def make_user_move(board,row,col):
    '''This function takes the parameter variables of the board,row,and column values and is 
    called when the user needs to make a move the row and col values provide restrictions 
    to ensure the move is valid. The numbers are then assigned to the nested list'''
    
    valid_move = False
    while valid_move==False:
        choice = input("What col would you like to move to (0-"+str(col-1)+"):")
        if choice.isdigit()==True and int(choice) >=0 and int(choice)<=col-1: 
            choice=int(choice)
            if board[0][choice]!= " ":
                print("Column is filled")
            for line in range(row-1,-1,-1):
                if board[line][choice] ==" ": 
                    board[line][choice] = 'X'
                    valid_move = True 
                    break
        else:
            print("Invalid Answer")
            
def make_computer_move(board,row,col):
    '''This function takes the parameter variables of the board,row,and column values 
    and is called when the computer needs to make a move. The row and col values provide 
    restrictions to ensure the move is valid. The computer uses a random number generator 
    to determine the computers move.  The numbers are then assigned to the nested list.'''
    
    import random 
    valid_move = False
    while valid_move==False:
        choice=random.randint(0,col-1)
        if choice >= 0 and choice<=col-1: 
            if board[0][choice]!= " ":
                valid_move=False
            for line in range(row-1,-1,-1):
                if board[line][choice] ==" ": 
                    board[line][choice] = 'O'
                    valid_move = True 
                    break


def main():
    '''This function defines the mainline logic of the program.''' 
    users_turn=True
    print("W E L C O M E   T O   C O N N E C T   F O U R!\n")
    display_hall_of_fame()
    
    print("\nThis Connect Four game allows you to choose")
    print("the amount of rows and columns you want.")
    print("You will be 'X' and I will be 'O'.\n")
    
    #Asks the user if they want to go first or not
    while True:
        turn=input("Would you like to go first? (y/n): ")
        if turn =="y" or turn=="Y":
            break
        elif turn =="N" or turn=="n":
            users_turn=False
            break
        else:
            print("Invalid Response")    
    
    #Takes user input to determine the rows and columns in the connect 4 grid
    while True:
        row=input("How many rows do you want:")  
        col=input("How many col do you want:")   
        if row.isdigit()==True and col.isdigit()==True:
            if int(row)>=4 and int(col)>=4:
                row=int(row)
                col=int(col)
                create_board(row,col)
                break
            else:
                print("Row and/or Col is too small.  We also only accepts values from 4-10")
                print("")
        else:
            print("Invalid Response, type integers for both")
            print("")
    
    #board,row,col are given values from the create_board() function and number
    # of free cells is determined from the row and col values
    board,row,col=create_board(row,col)   
    free_cells=row*col

    #This loop continues to run if a winner is not called and the free cells is greater than 0.
    while not get_winner(board,row,col) and free_cells>0:
        if users_turn==True: 
            display_board(board,row,col) 
            make_user_move(board,row,col)
            users_turn = False
        elif users_turn==False:
            make_computer_move(board,row,col)
            users_turn = True
        free_cells -= 1
    
    #When a winner,loser, or stalemate is acheived.  One of theses options will be shown
    display_board(board,row,col) 
    if (get_winner(board,row,col) == 'X'):
        print("Y O U   W O N !")
        add_to_hall_of_fame()
    elif (get_winner(board,row,col) == 'O'):
        print("I   W O N !")
        print("I   A M   I N V I N C I B L E !")
    else:
        print("S T A L E M A T E !")
    print("\n*** GAME OVER ***\n")
    
main()
