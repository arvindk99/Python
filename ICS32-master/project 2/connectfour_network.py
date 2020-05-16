import connectfour_protocol
import connectfour_tools
import connectfour
from collections import namedtuple



def loginuser()-> 'username':
    '''This function receives an input from the user, and if
    the input is a valid string, returns username, if not, asks
    to enter a valid string'''
    while True:
        try:
            username = input("Enter username of your choice: ")
            if username == '':
                username = (input("Enter a valid username: "))
            else:
                return username.strip('')
        except TypeError:
            print("Enter a string.")
            

def clientmove(col, move) -> 'movecol':
    '''This function takes a column number and move then combines the two
        and returns the combination as a string.'''
    movecol = str(move + ' {}'.format(col+1))
    return movecol


def netmovechecker(gamestate,column,move) -> 'current_gamestate':
    '''This function will take in the current gamestate, column and move input
        of the server and perform the move. If the move is invalid, it will
         raise a GameOverError, break, and close the connection'''
    while True:
        try:
            if move == 'DROP':
                current_gamestate = connectfour.drop(gamestate, column)
                print("MOVE: " + move + ' {}'.format(column + 1))
                return current_gamestate
            
            elif move == 'POP':
                current_gamestate = connectfour.pop(gamestate, column)
                print("MOVE: " + move + ' {}'.format(column + 1))
                return current_gamestate

        except connectfour.InvalidMoveError:
            raise connectfour.GameOverError
        except connectfour.GameOverError:
            print("Game is over.")
            break

def clientmovechecker(gamestate) -> 'current_gamestate, movecol':
    ''' This function will take in the current gamestate, then it will ask the user
        for a column and move input, if the move is invalid, it will ask the user to
        to reinput the column and move. If it is valid, perform the move and return
        a new gamestate and the move and column combined as a str.'''
    column = connectfour_tools.columninput()
    move = connectfour_tools.moveinput()
    while True:
        try:
            if move == 'DROP':
                current_gamestate = connectfour.drop(gamestate, column)
                print("MOVE: " + move + ' {}'.format(column + 1))
                movecol = str(move + ' {}'.format(column + 1))
                return current_gamestate, movecol
            elif move == 'POP':
                current_gamestate = connectfour.pop(gamestate, column)
                print("MOVE: " + move + ' {}'.format(column + 1))
                movecol = str(move + ' {}'.format(column + 1))
                return current_gamestate, movecol

        except connectfour.InvalidMoveError:
            print("INVALID MOVE.")
            column = connectfour_tools.columninput()
            move = connectfour_tools.moveinput()
        except connectfour.GameOverError:
            print("Game is over.")
            break






def network():
    '''Takes functions from the protocol and tools module in order
    to run the network version of the game. First it will start the connection and ask the user
    for a username. If the username is valid, it will then start an AI_game automatically.
    Once the game starts it will loop between the client turn and server turn'''
    connection = connectfour_protocol.startconnection()
    username = loginuser()
    welcomemessage = connectfour_protocol.welcomelogin(connection, username)
    print(welcomemessage)
    turn = connectfour_protocol.startaigame(connection)
    gamestate = connectfour_tools.gamestart()

    
    while True:
        try:
            if turn == connectfour.RED:
                print("User's turn.")
                gamestate, movecol = clientmovechecker(gamestate)
                connectfour_protocol.sendmessage(connection, movecol)
                connectfour_tools.gameboard(gamestate)
                turn = connectfour_protocol.turncolor(connection)

            if turn == connectfour.YELLOW:
                serverturn = connectfour_protocol.servermove(connection)
                col = serverturn[1]
                move = serverturn[0]
                gamestate = netmovechecker(gamestate,col,move)
                connectfour_tools.gameboard(gamestate)
                turn = connectfour_protocol.turncolor(connection)
                
            if turn == 11:
                print("Red player wins.")
                raise connectfour.GameOverError
            if turn == 22:
                print("Yellow player wins.")
                raise connectfour.GameOverError

        except connectfour.GameOverError:
            print("Connection closing...")
            connectfour_protocol.close(connection)
            break


if __name__ == '__main__':
    network()
