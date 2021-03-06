import connectfour

def columninput() -> int:
    ''' This function asks a user for a column number,
        and if the number is between 1 and 7, return the number'''
    while True:

        try:
            column = int(input("Enter a column number between 1 and 7: "))
            while column < 1 or column >7:
                print("INVALID")
                column = int(input("Enter a valid column number between 1 and 7: "))

        except ValueError:
            print("INVALID")

        else:
            return column - 1

def moveinput()-> str:
    '''This function is so that the player can carry out the move.
    It takes in an input of either drop or pop and according to the input
    and then it returns the result.'''
    while True:
        move = str(input("drop or pop?: "))

        if move == 'drop':
            move = move.upper()
            return move

        elif move == 'pop':
            move = move.upper()
            return move

        else:
            print("INVALID")

def gameboard(gamestate)-> None:
    ''' This function is only for visualization purposes.
        It will take in the current gamestate
        and output a connect four board'''
    gameboard = gamestate.board
    print("1  2  3  4  5  6  7")
    spotindex = 0
    printcount = 0
    while spotindex <= 5:
        
        'x = spotindex'
        boardrow = [spot[spotindex] for spot in gameboard]
        while printcount <= 6:
            for i in boardrow:
                if i == 1:
                    print("R  ",end='')
                    printcount += 1
                elif i == 2:
                    print("Y  ",end='')
                    printcount += 1
                else:
                    print(".  ",end='')
                    printcount += 1
                    
        spotindex += 1
        print()
        printcount -= 6

def gamestart()->'gamestate':
    '''Function opens up the game board from the connectfour module.'''
    gamestate = connectfour.new_game()
    gameboard(gamestate)
    return gamestate


def turnchecker(gamestate)->int:
    '''This function takes in the current gamestate
       and returns the color of the current turn'''
    currentgamestate = gamestate
    turn = currentgamestate.turn
    return turn


